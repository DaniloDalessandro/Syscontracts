from datetime import datetime
from decimal import Decimal
from django.db import models
from django.forms import ValidationError
from centers.models import CentroDeCustoGestor,CentroDeCustoSolicitante
from budgets.models import Orcamento
from collaborators.models import Colaborador
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models import Sum


#=============================================================================================================================================
class LinhaOrcamentaria(models.Model):
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True, verbose_name='Tipo de linha')

    CUSTODESPESA_CHOICES = [
        ('A', 'Base Principal'),
        ('B', 'Serviços Especializados'),
        ('C', 'Despesas Compartilhadas'),
        # Outros valores...
    ]
    custo_despesa = models.CharField(max_length=100, choices=CUSTODESPESA_CHOICES, verbose_name='CUSTO/DESPESA')

    centro_custo_gestor = models.ForeignKey(CentroDeCustoGestor, on_delete=models.SET_NULL, null=True, blank=True)
    centro_custo_solicitante = models.ForeignKey(CentroDeCustoSolicitante, on_delete=models.SET_NULL, null=True, blank=True)
    descricao_resumida = models.CharField(max_length=255, null=True, blank=True, verbose_name='Finalidade')
    objeto = models.CharField(max_length=80, blank=True, null=True, verbose_name='Objeto')

    CLASSIFICACAO_CHOICES = [
        ('NOVO', 'NOVO'),
        ('RENOVAÇÃO', 'RENOVAÇÃO'),
        ('CARY OVER', 'CARY OVER'),
        ('REPLANEJAMENTO', 'REPLANEJAMENTO'),
        ('N/A', 'N/A'),
    ]
    classificacao_orcamento = models.CharField(max_length=100, choices=CLASSIFICACAO_CHOICES, null=True, blank=True)

    possivel_fiscal = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_possivel', verbose_name='Fiscal')

    ano_orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)
    TIPOCONTRATO_CHOICES = [
        ('SERVIÇO', 'SERVIÇO'),
        ('FORNECIMENTO', 'FORNECIMENTO'),
        ('ASSINATURA', 'ASSINATURA'),
        ('FORNECIMENTO/SERVIÇO', 'FORNECIMENTO/SERVIÇO'),
    ]
    tipo_contrato = models.CharField(max_length=100, choices=TIPOCONTRATO_CHOICES, blank=True, null=True)

    STATUS_LINHA_ORCAMENTARIA_CHOICES = [
        ('I', 'SERVIÇO'),
        ('II', 'FORNECIMENTO'),
        ('III', 'ASSINATURA'),
        ('IV', 'FORNECIMENTO/SERVIÇO'),
    ]
    status_linha_orcamentaria = models.CharField(max_length=100, choices=STATUS_LINHA_ORCAMENTARIA_CHOICES, blank=True, null=True)

    TIPOCONTRATACAOPROVAVEL_CHOICES = [
        ('A', 'LICITAÇÃO'),
        ('B', 'DISPENSA EM RAZÃO DO VALOR'),
        ('C', 'CONVÊNIO'),
        ('D', 'FUNDO FIXO'),
        ('E', 'INEXIGIBILIDADE'),
        ('F', 'ATA DE REGISTRO DE PREÇO'),
        ('H', 'ACORDO DE COOPERAÇÃO'),
        ('I', 'APOSTILAMENTO'),
    ]
    tipo_provavel_contratacao = models.CharField(max_length=100, choices=TIPOCONTRATACAOPROVAVEL_CHOICES)
    valor_orcado = models.FloatField(default=0, blank=True, null=True,validators=[MinValueValidator(0.01)])

    STATUSELABORACAOTR_CHOICES = [
        ('VENCIDO', 'VENCIDO'),
        ('DENTRO DO PRAZO', 'DENTRO DO PRAZO'),
        ('ELABORADO COM ATRASO', 'ELABORADO COM ATRASO'),
        ('ELABORADO NO PRAZO', 'ELABORADO NO PRAZO'),
    ]
    status_elaboracao_tr = models.CharField(max_length=100, choices=STATUSELABORACAOTR_CHOICES, blank=True, null=True)

    necessidade_contratacao = models.DateField(blank=True, null=True)

    STATUSPROCESSO_CHOICES = [
        ('I', 'PLANEJAMENTO'),
        ('II', 'Execução'),
        ('III', 'Elaboração de TR'),
        ('IV', 'Cotação'),
        ('V', 'Em proc. aditivo'),
    ]
    status_processo = models.CharField(max_length=100, choices=STATUSPROCESSO_CHOICES, blank=True, null=True)

    STATUSCONTRATACAO_CHOICES = [
        ('A', 'DENTRO DO PRAZO'),
        ('B', 'CONTRATADO NO PRAZO'),
        ('C', 'CONTRATADO COM ATRASO'),
        ('D', 'PRAZO VENCIDO'),
        ('E', 'LINHA TOTALMENTE REMANEJADA'),
        ('F', 'LINHA TOTALMENTE EXECUTADA'),
        ('G', 'LINHA DE PAGAMENTO'),
        ('H', 'LINHA PARCIALMENTE REMANEJADA'),
        ('I', 'LINHA PARCIALMENTE EXECUTADA'),
        ('J', 'N/A'),
    ]
    status_contratacao = models.CharField(max_length=100, choices=STATUSCONTRATACAO_CHOICES, blank=True, null=True)
    obs_contrato = models.TextField(max_length=400, blank=True, null=True)

    def saldo_disponivel(self):
        total_contratos = self.contratos.aggregate(total=Sum('valor_contrato'))['total'] or Decimal('0.0')
        saldo = Decimal(self.valor_orcado) - total_contratos
        return saldo
        
    def save(self, *args, **kwargs):
        if self.ano_orcamento and self.valor_orcado > self.ano_orcamento.valor_restante:
            raise ValidationError('O valor orçado excede o valor restante do orçamento.')
        super().save(*args, **kwargs)

    
    @property
    def valor_remanejado_total(self):
        remanejamentos_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        remanejamentos_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        return remanejamentos_origem + remanejamentos_destino

    @property
    def saldo_orcamentario_pos_remanejamento(self):
        valor_remanejado_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        valor_remanejado_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        saldo = Decimal(self.valor_orcado) + valor_remanejado_destino - valor_remanejado_origem - Decimal(self.valor_utilizado)
        return saldo

    @property
    def tempo_para_contratacao(self):
        if self.necessidade_contratacao:
            dias_restantes = (self.necessidade_contratacao - datetime.now().date()).days
            return max(dias_restantes, 0)
        return None

    def __str__(self):
        return self.descricao_resumida or "Linha sem descrição"

    class Meta:
        verbose_name = 'Linha Orçamentária'
        verbose_name_plural = 'Linhas Orçamentárias'


# ============================================================================================================


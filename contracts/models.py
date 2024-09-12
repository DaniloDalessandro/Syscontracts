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

    def __str__(self):
        return self.descricao_resumida or "Linha sem descrição"

    class Meta:
        verbose_name = 'Linha Orçamentária'
        verbose_name_plural = 'Linhas Orçamentárias'


# ============================================================================================================

class Contrato(models.Model):
    linha_orcamentaria = models.ForeignKey(LinhaOrcamentaria, on_delete=models.PROTECT, related_name='contratos')
    numero_protocolo = models.CharField(max_length=7, unique=True, blank=True, editable=False, verbose_name='Contrato')
    data_assinatura = models.DateField(null=True, blank=True)
    data_vencimento = models.DateField(null=True, blank=True)
    fiscal_principal = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_principal', verbose_name='Fiscal Principal')
    fiscal_substituto = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_substituto', verbose_name='Fiscal Substituto')
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2)
    TIPO_PAGAMENTO_CHOICES = [
        ('PAGAMENTO ÚNICO','PAGAMENTO ÚNICO'),
        ('PAGAMENTO ANUAL','PAGAMENTO ANUAL'),
        ('PAGAMENTO SEMANAL','PAGAMENTO SEMANAL'),
        ('PAGAMENTO MENSAL','PAGAMENTO MENSAL'),
        ('PAGAMENTO QUIZENAL','PAGAMENTO QUINZENAL'),
        ('PAGAMENTO TRIMESTRAL','PAGAMENTO TRIMESTRAL'),
        ('PAGAMENTO SEMESTRAL','PAGAMENTO SEMESTRAL'),
        ('PAGAMENTO SOB DEMANDA','PAGAMENTO SOB DEMANDA'),
    ]
    natureza_pagamento = models.CharField(choices=TIPO_PAGAMENTO_CHOICES,max_length=30)
       
    def generate_protocolo(self):
        year_suffix = timezone.now().year % 100
        last_protocolo = Contrato.objects.filter(numero_protocolo__endswith=f"/{year_suffix}").order_by('id').last()
        
        if last_protocolo:
            last_sequence = int(last_protocolo.numero_protocolo.split('/')[0])
            new_sequence = f"{last_sequence + 1:04}"
        else:
            new_sequence = "0001"

        return f"{new_sequence}/{year_suffix}"
    
    def __str__(self):
        return self.numero_protocolo or "Linha Orçamentária sem Descrição"
    
#===============================================================================================================================

class Prestacao(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    numero_parcela = models.PositiveIntegerField(editable=False)  # O número da parcela será gerado automaticamente
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    data_pagamento = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Se for uma nova prestação (sem ID)
            # Verifica quantas prestações já existem para este contrato
            total_prestacoes = Prestacao.objects.filter(contrato=self.contrato).count()
            # Define o próximo número da parcela
            self.numero_parcela = total_prestacoes + 1

        super(Prestacao, self).save(*args, **kwargs)

#===============================================================================================================================
    
class Remanejamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)])
    linha_origem = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_origem', on_delete=models.CASCADE)
    linha_destino = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_destino', on_delete=models.CASCADE)
    data_remanejamento = models.DateTimeField(default=timezone.now)
    motivo = models.TextField()
    
    class Meta:
        verbose_name = 'Remanejamento'
        verbose_name_plural = 'Remanejamentos'

#===============================================================================================================================

class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='aditivos')
    data = models.DateField(null=True,blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,default=0.0)
    justificativa = models.CharField(max_length=150)

    
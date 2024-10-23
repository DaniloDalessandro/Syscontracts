from django.db import models
from centers.models import CentroDeCustoGestor
from django.db.models import Sum
from django.core.validators import MinValueValidator
from decimal import Decimal

#===================================================================================================================
class Orcamento(models.Model):
    ano = models.IntegerField()
    centro = models.ForeignKey(CentroDeCustoGestor, on_delete=models.CASCADE)
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0,validators=[MinValueValidator(0.01)] )

    @property
    def valores_adicionados(self):
        if self.pk:
            return self.orcamentos_externos.filter(tipo_movimentacao='entrada').aggregate(total=Sum('valor'))['total'] or 0
        return 0

    @property
    def valores_enviados(self):
        if self.pk:
            return self.orcamentos_externos.filter(tipo_movimentacao='retirada').aggregate(total=Sum('valor'))['total'] or 0
        return 0

    @property
    def valor_total(self):
        if self.pk:
            return self.valor + self.valores_adicionados - self.valores_enviados
        return self.valor

    @property
    def orcamento_total(self):
        if self.pk:
            orcamentos_internos = Orcamento.objects.filter(ano=self.ano, centro=self.centro).aggregate(total=Sum('valor'))['total'] or 0
            orcamentos_externos = OrcamentoExterno.objects.filter(ano=self).aggregate(total=Sum('valor'))['total'] or 0
            return orcamentos_internos + orcamentos_externos
        return self.valor
    
    @property
    def valor_restante(self):
        linhas_orcamentarias = self.contratos.all()  
        total_linhas = sum(Decimal(linha.valor_orcado) for linha in linhas_orcamentarias)
        return self.valor - total_linhas

    def __str__(self):
        return f"{self.ano} - {self.centro}"

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
        unique_together = ('ano', 'centro', 'classe')

# ============================================================================================================

class OrcamentoExterno(models.Model):
    ENTRADA_RETIRADA_CHOICES = [
        ('entrada', 'Entrada'),
        ('retirada', 'Retirada'),
    ]

    ano = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='orcamentos_externos')
    valor = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)])
    centro = models.CharField(max_length=20)
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)
    tipo_movimentacao = models.CharField(max_length=8, choices=ENTRADA_RETIRADA_CHOICES)

    def save(self, *args, **kwargs):
        # Verifica se o orçamento principal já foi salvo
        if not self.ano.pk:
            self.ano.save()

        # Armazena valores antigos antes de salvar
        old_valor = None
        old_tipo_movimentacao = None
        if self.pk:
            old_instance = OrcamentoExterno.objects.get(pk=self.pk)
            old_valor = old_instance.valor
            old_tipo_movimentacao = old_instance.tipo_movimentacao

        super().save(*args, **kwargs)

        # Atualiza o valor do orçamento principal
        if old_valor is not None and old_tipo_movimentacao is not None:
            if old_tipo_movimentacao == 'entrada':
                self.ano.valor -= old_valor
            elif old_tipo_movimentacao == 'retirada':
                self.ano.valor += old_valor

        if self.tipo_movimentacao == 'entrada':
            self.ano.valor += self.valor
        elif self.tipo_movimentacao == 'retirada':
            self.ano.valor -= self.valor

        self.ano.save()

    def delete(self, *args, **kwargs):
        # Atualizar orçamento ao deletar
        if self.tipo_movimentacao == 'entrada':
            self.ano.valor -= self.valor
        elif self.tipo_movimentacao == 'retirada':
            self.ano.valor += self.valor
        self.ano.save()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Orçamento Externo'
        verbose_name_plural = 'Orçamentos Externos'

    def __str__(self):
        return f"{self.ano} - {self.centro} - {self.get_tipo_movimentacao_display()}"
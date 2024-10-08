from django.db import models
from collaborators.models import Colaborador
from contracts.models import LinhaOrcamentaria
from django.db.models import F
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator

class AuxilioColaborador(models.Model):
    beneficiado = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    linha = models.ForeignKey(LinhaOrcamentaria, related_name='auxilios_colaboradores', on_delete=models.PROTECT)
    tipo_choices = [
        ('Graduação', 'Graduação'),
        ('Pós-Graduação', 'Pós-Graduação'),
        ('Auxílio creche escola', 'Auxílio creche escola'),
        ('Língua estrangeira', 'Língua estrangeira'),
    ]
    tipo = models.CharField(max_length=100, choices=tipo_choices, null=True, blank=True)
    beneficio = models.CharField(max_length=100, blank=False)
    valor_parcela = models.FloatField(null=True, blank=True)
    valor_total = models.FloatField(null=True, blank=True, editable=False, validators=[MinValueValidator(0.01)])
    obs = models.CharField(max_length=200, null=True, blank=True)
    mes_inicio = models.DateField(null=True, blank=True)
    qtd_parcelas = models.PositiveIntegerField()
    mes_fim = models.DateField(editable=False, null=True, blank=True)
    previsao_inicio = models.DateField(default='2024-09-16', blank=True, null=True)
    status_choices = [
        ('aguardando', 'Aguardando'),
        ('ativo', 'Ativo'),
        ('ativo_com_atraso', 'Ativo com Atraso'),
        ('finalizado', 'Finalizado'),
        ('aguardando_com_atraso', 'Aguardando com Atraso'),
    ]
    status = models.CharField(max_length=30, choices=status_choices, default='aguardando')

    def save(self, *args, **kwargs):
        # Calcular valor_total como a soma de todas as parcelas
        if self.valor_parcela and self.qtd_parcelas:
            self.valor_total = self.valor_parcela * self.qtd_parcelas
        
        # Calcular mes_fim com base em mes_inicio e qtd_parcelas
        if self.mes_inicio and self.qtd_parcelas:
            self.mes_fim = self.mes_inicio + relativedelta(months=self.qtd_parcelas)
        
        # Atualizar o status com base nas datas
        hoje = date.today()

        if self.previsao_inicio:
            if not self.mes_inicio:
                if hoje < self.previsao_inicio:
                    self.status = 'aguardando_com_atraso'
                else:
                    self.status = 'aguardando'
            elif self.mes_inicio:
                if hoje < self.mes_inicio:
                    self.status = 'aguardando'
                elif self.mes_inicio > self.previsao_inicio:
                    if self.mes_inicio <= hoje <= self.mes_fim:
                        self.status = 'ativo_com_atraso'
                    elif hoje > self.mes_fim:
                        self.status = 'finalizado'
                else:
                    if self.mes_inicio <= hoje <= self.mes_fim:
                        self.status = 'ativo'
                    elif hoje > self.mes_fim:
                        self.status = 'finalizado'
        else:
            if not self.mes_inicio:
                self.status = 'aguardando'
            elif self.mes_inicio:
                if hoje < self.mes_inicio:
                    self.status = 'aguardando'
                elif self.mes_inicio <= hoje <= self.mes_fim:
                    self.status = 'ativo'
                elif hoje > self.mes_fim:
                    self.status = 'finalizado'

        super().save(*args, **kwargs)
   
    class Meta:
        verbose_name = 'Auxílio Colaborador'
        verbose_name_plural = 'Auxílios Colaboradores'
        unique_together = ('beneficiado', 'linha', 'tipo', 'beneficio')

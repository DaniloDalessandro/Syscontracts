# Generated by Django 5.1.1 on 2024-09-11 16:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budgets', '0002_alter_orcamento_classe'),
        ('centers', '0002_centrodecustosolicitante'),
        ('collaborators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinhaOrcamentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.CharField(blank=True, choices=[('OPEX', 'OPEX'), ('CAPEX', 'CAPEX')], max_length=100, null=True, verbose_name='Tipo de linha')),
                ('custo_despesa', models.CharField(choices=[('A', 'Base Principal'), ('B', 'Serviços Especializados'), ('C', 'Despesas Compartilhadas')], max_length=100, verbose_name='CUSTO/DESPESA')),
                ('descricao_resumida', models.CharField(blank=True, max_length=255, null=True, verbose_name='Finalidade')),
                ('objeto', models.CharField(blank=True, max_length=80, null=True, verbose_name='Objeto')),
                ('classificacao_orcamento', models.CharField(blank=True, choices=[('NOVO', 'NOVO'), ('RENOVAÇÃO', 'RENOVAÇÃO'), ('CARY OVER', 'CARY OVER'), ('REPLANEJAMENTO', 'REPLANEJAMENTO'), ('N/A', 'N/A')], max_length=100, null=True)),
                ('tipo_contrato', models.CharField(blank=True, choices=[('SERVIÇO', 'SERVIÇO'), ('FORNECIMENTO', 'FORNECIMENTO'), ('ASSINATURA', 'ASSINATURA'), ('FORNECIMENTO/SERVIÇO', 'FORNECIMENTO/SERVIÇO')], max_length=100, null=True)),
                ('status_linha_orcamentaria', models.CharField(blank=True, choices=[('I', 'SERVIÇO'), ('II', 'FORNECIMENTO'), ('III', 'ASSINATURA'), ('IV', 'FORNECIMENTO/SERVIÇO')], max_length=100, null=True)),
                ('tipo_provavel_contratacao', models.CharField(choices=[('A', 'LICITAÇÃO'), ('B', 'DISPENSA EM RAZÃO DO VALOR'), ('C', 'CONVÊNIO'), ('D', 'FUNDO FIXO'), ('E', 'INEXIGIBILIDADE'), ('F', 'ATA DE REGISTRO DE PREÇO'), ('H', 'ACORDO DE COOPERAÇÃO'), ('I', 'APOSTILAMENTO')], max_length=100)),
                ('valor_orcado', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('status_elaboracao_tr', models.CharField(blank=True, choices=[('I', 'VENCIDO'), ('II', 'DENTRO DO PRAZO'), ('III', 'ELABORADO COM ATRASO'), ('IV', 'ELABORADO NO PRAZO')], max_length=100, null=True)),
                ('necessidade_contratacao', models.DateField(blank=True, null=True)),
                ('status_processo', models.CharField(blank=True, choices=[('I', 'PLANEJAMENTO'), ('II', 'Execução'), ('III', 'Elaboração de TR'), ('IV', 'Cotação'), ('V', 'Em proc. aditivo')], max_length=100, null=True)),
                ('status_contratacao', models.CharField(blank=True, choices=[('A', 'DENTRO DO PRAZO'), ('B', 'CONTRATADO NO PRAZO'), ('C', 'CONTRATADO COM ATRASO'), ('D', 'PRAZO VENCIDO'), ('E', 'LINHA TOTALMENTE REMANEJADA'), ('F', 'LINHA TOTALMENTE EXECUTADA'), ('G', 'LINHA DE PAGAMENTO'), ('H', 'LINHA PARCIALMENTE REMANEJADA'), ('I', 'LINHA PARCIALMENTE EXECUTADA'), ('J', 'N/A')], max_length=100, null=True)),
                ('obs_contrato', models.TextField(blank=True, max_length=400, null=True)),
                ('ano_orcamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='budgets.orcamento')),
                ('centro_custo_gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centers.centrodecustogestor')),
                ('centro_custo_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centers.centrodecustosolicitante')),
                ('possivel_fiscal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_possivel', to='collaborators.colaborador', verbose_name='Fiscal')),
            ],
            options={
                'verbose_name': 'Linha Orçamentária',
                'verbose_name_plural': 'Linhas Orçamentárias',
            },
        ),
    ]

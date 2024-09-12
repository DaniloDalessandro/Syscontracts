# Generated by Django 5.1.1 on 2024-09-12 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborators', '0001_initial'),
        ('contracts', '0002_alter_linhaorcamentaria_status_elaboracao_tr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_protocolo', models.CharField(blank=True, editable=False, max_length=7, unique=True, verbose_name='Contrato')),
                ('data_assinatura', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('valor_contrato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('natureza_pagamento', models.CharField(choices=[('PAGAMENTO ÚNICO', 'PAGAMENTO ÚNICO'), ('PAGAMENTO ANUAL', 'PAGAMENTO ANUAL'), ('PAGAMENTO SEMANAL', 'PAGAMENTO SEMANAL'), ('PAGAMENTO MENSAL', 'PAGAMENTO MENSAL'), ('PAGAMENTO QUIZENAL', 'PAGAMENTO QUINZENAL'), ('PAGAMENTO TRIMESTRAL', 'PAGAMENTO TRIMESTRAL'), ('PAGAMENTO SEMESTRAL', 'PAGAMENTO SEMESTRAL'), ('PAGAMENTO SOB DEMANDA', 'PAGAMENTO SOB DEMANDA')], max_length=30)),
                ('fiscal_principal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_principal', to='collaborators.colaborador', verbose_name='Fiscal Principal')),
                ('fiscal_substituto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_substituto', to='collaborators.colaborador', verbose_name='Fiscal Substituto')),
                ('linha_orcamentaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='contracts.linhaorcamentaria')),
            ],
        ),
    ]

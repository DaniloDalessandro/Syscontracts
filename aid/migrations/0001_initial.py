# Generated by Django 5.1.1 on 2024-09-14 02:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collaborators', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuxilioColaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('Graduação', 'Graduação'), ('Pós-Graduação', 'Pós-Graduação'), ('Auxílio creche escola', 'Auxílio creche escola'), ('Língua estrangeira', 'Língua estrangeira')], max_length=100, null=True)),
                ('beneficio', models.CharField(max_length=100)),
                ('valor_parcela', models.FloatField(blank=True, null=True)),
                ('valor_total', models.FloatField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('mes_inicio', models.DateField()),
                ('qtd_parcelas', models.PositiveIntegerField()),
                ('mes_fim', models.DateField(editable=False)),
                ('status', models.CharField(choices=[('aguardando', 'Aguardando'), ('ativo', 'Ativo'), ('finalizado', 'Finalizado')], default='aguardando', max_length=10)),
                ('beneficiado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collaborators.colaborador')),
                ('linha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='auxilios_colaboradores', to='contracts.linhaorcamentaria')),
            ],
            options={
                'verbose_name': 'Auxílio Colaborador',
                'verbose_name_plural': 'Auxílios Colaboradores',
                'unique_together': {('beneficiado', 'linha', 'tipo', 'beneficio')},
            },
        ),
    ]

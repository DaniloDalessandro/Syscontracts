# Generated by Django 5.1.1 on 2024-09-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0002_auxiliocolaborador_previsao_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='mes_fim',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='mes_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='status',
            field=models.CharField(choices=[('aguardando', 'Aguardando'), ('ativo', 'Ativo'), ('ativo_com_atraso', 'Ativo com Atraso'), ('finalizado', 'Finalizado'), ('aguardando_com_atraso', 'Aguardando com Atraso')], default='aguardando', max_length=30),
        ),
    ]

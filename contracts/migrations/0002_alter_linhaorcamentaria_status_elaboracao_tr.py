# Generated by Django 5.1.1 on 2024-09-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linhaorcamentaria',
            name='status_elaboracao_tr',
            field=models.CharField(blank=True, choices=[('VENCIDO', 'VENCIDO'), ('DENTRO DO PRAZO', 'DENTRO DO PRAZO'), ('ELABORADO COM ATRASO', 'ELABORADO COM ATRASO'), ('ELABORADO NO PRAZO', 'ELABORADO NO PRAZO')], max_length=100, null=True),
        ),
    ]
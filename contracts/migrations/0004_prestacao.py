# Generated by Django 5.1.1 on 2024-09-12 13:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_parcela', models.PositiveIntegerField(editable=False)),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.contrato')),
            ],
        ),
    ]

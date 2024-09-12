# Generated by Django 5.1.1 on 2024-09-12 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_remanejamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aditivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('justificativa', models.CharField(max_length=150)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aditivos', to='contracts.contrato')),
            ],
        ),
    ]

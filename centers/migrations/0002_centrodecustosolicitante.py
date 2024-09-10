# Generated by Django 5.1.1 on 2024-09-10 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeCustoSolicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('centro_gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitantes', to='centers.centrodecustogestor')),
            ],
            options={
                'unique_together': {('centro_gestor', 'nome')},
            },
        ),
    ]

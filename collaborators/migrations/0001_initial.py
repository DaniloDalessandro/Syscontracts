# Generated by Django 5.1.1 on 2024-09-11 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sectors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100, null=True)),
                ('mat', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Matrícula')),
                ('ramal', models.CharField(blank=True, max_length=4, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('coordenacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sectors.coordenacao')),
                ('direcao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sectors.direcao')),
                ('gerencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sectors.gerencia')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
    ]

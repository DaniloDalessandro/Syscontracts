# Generated by Django 5.1.1 on 2024-09-10 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Direção',
                'verbose_name_plural': 'Direções',
            },
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('direcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerencias', to='sectors.direcao')),
            ],
            options={
                'verbose_name': 'Gerência',
                'verbose_name_plural': 'Gerências',
                'unique_together': {('direcao', 'nome')},
            },
        ),
        migrations.CreateModel(
            name='Coordenacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('gerencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordenacoes', to='sectors.gerencia')),
            ],
            options={
                'verbose_name': 'Coordenação',
                'verbose_name_plural': 'Coordenações',
                'unique_together': {('gerencia', 'nome')},
            },
        ),
    ]
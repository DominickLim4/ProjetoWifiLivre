# Generated by Django 5.0 on 2023-12-19 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=14)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroConexao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_conexao', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('informacoes_adicionais', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wifi.usuario')),
            ],
        ),
    ]
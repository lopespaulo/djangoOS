# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('primeiro_nome', models.CharField(verbose_name='primeiro nome', max_length=60)),
                ('ultimo_nome', models.CharField(blank=True, verbose_name='ultimo nome', max_length=60, null=True)),
                ('telefone', models.CharField(blank=True, verbose_name='telefone', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, verbose_name='email', max_length=75, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oservico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('data_abertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipamento', models.TextField(blank=True)),
                ('defeito', models.TextField(blank=True)),
                ('situacao', models.CharField(default='A', max_length=1, choices=[('A', 'Aberta'), ('F', 'Fechada'), ('C', 'Cancelada')])),
                ('solucao', models.TextField(blank=True)),
                ('data_fechamento', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(to='rango.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Ordens de Serviço',
                'verbose_name': 'Ordem de Serviço',
            },
            bases=(models.Model,),
        ),
    ]

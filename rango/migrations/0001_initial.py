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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('primeiro_nome', models.CharField(max_length=60, verbose_name='primeiro nome')),
                ('ultimo_nome', models.CharField(max_length=60, verbose_name='ultimo nome', null=True, blank=True)),
                ('telefone', models.CharField(max_length=15, verbose_name='telefone', null=True, blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oservico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('data_abertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipamento', models.TextField(blank=True)),
                ('defeito', models.TextField(blank=True)),
                ('situacao', models.CharField(max_length=1, default='A', choices=[('A', 'Aberta'), ('F', 'Fechada'), ('C', 'Cancelada')])),
                ('cliente', models.ForeignKey(to='rango.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Ordens de Serviço',
                'verbose_name': 'Ordem de Serviço',
            },
            bases=(models.Model,),
        ),
    ]

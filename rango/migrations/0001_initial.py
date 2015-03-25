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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('primeiro_nome', models.CharField(max_length=60)),
                ('ultimo_nome', models.CharField(max_length=60, blank=True, null=True)),
                ('telefone', models.CharField(max_length=15, blank=True, null=True)),
                ('email', models.EmailField(max_length=75, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oservico',
            fields=[
                ('numero_os', models.AutoField(serialize=False, primary_key=True)),
                ('data_abertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipamento', models.TextField(blank=True)),
                ('defeito', models.TextField(blank=True)),
                ('situacao', models.CharField(max_length=1, choices=[('A', 'Aberta'), ('F', 'Fechada'), ('C', 'Cancelada')])),
                ('cliente', models.ForeignKey(to='rango.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Ordens de Serviço',
                'verbose_name': 'Ordem de Serviço',
            },
            bases=(models.Model,),
        ),
    ]

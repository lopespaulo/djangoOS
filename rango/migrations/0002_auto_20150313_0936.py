# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(null=True, max_length=75, blank=True, verbose_name='email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primeiro_nome',
            field=models.CharField(max_length=60, verbose_name='primeiro nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(null=True, max_length=15, blank=True, verbose_name='telefone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ultimo_nome',
            field=models.CharField(null=True, max_length=60, blank=True, verbose_name='ultimo nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oservico',
            name='situacao',
            field=models.CharField(default='A', max_length=1, choices=[('A', 'Aberta'), ('F', 'Fechada'), ('C', 'Cancelada')]),
            preserve_default=True,
        ),
    ]

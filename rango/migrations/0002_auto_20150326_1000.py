# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oservico',
            name='data_fechamento',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oservico',
            name='solucao',
            field=models.TextField(blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oservico',
            name='defeito',
            field=models.TextField(blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oservico',
            name='equipamento',
            field=models.TextField(blank=True, max_length=500),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oservico',
            name='solucao',
        ),
        migrations.AlterField(
            model_name='oservico',
            name='data_fechamento',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oservico',
            name='defeito',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oservico',
            name='equipamento',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20150326_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='oservico',
            name='solucao',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

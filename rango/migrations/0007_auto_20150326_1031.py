# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20150326_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oservico',
            name='data_fechamento',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]

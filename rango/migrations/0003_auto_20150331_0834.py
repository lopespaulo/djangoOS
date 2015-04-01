# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150331_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oservico',
            name='data_fechamento',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]

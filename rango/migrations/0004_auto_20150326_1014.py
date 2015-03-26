# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20150326_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oservico',
            name='data_fechamento',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True),
            preserve_default=True,
        ),
    ]

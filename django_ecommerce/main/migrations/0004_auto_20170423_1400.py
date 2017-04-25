# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170423_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusreport',
            name='when',
            field=models.DateTimeField(blank=True),
        ),
    ]

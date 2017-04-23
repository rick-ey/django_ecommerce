# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangular_polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollitem',
            name='percentage',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
    ]

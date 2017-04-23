# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangular_polls', '0002_pollitem_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollitem',
            name='percentage',
        ),
    ]

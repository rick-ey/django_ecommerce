# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170424_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

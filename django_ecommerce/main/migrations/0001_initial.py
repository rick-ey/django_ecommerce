# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('when', models.DateTimeField(auto_now=True)),
                ('img', models.CharField(max_length=255, null=True)),
                ('vid', models.URLField(null=True)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MarketingItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=300)),
                ('caption', models.TextField()),
                ('button_link', models.URLField(null=True, default='register')),
                ('button_title', models.CharField(max_length=20, default='View details')),
            ],
        ),
    ]

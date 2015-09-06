# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='prices_url',
            field=models.CharField(unique=True, max_length=256, default='NONE'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(unique=True, max_length=128, default='NONE'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(unique=True, max_length=6, default='NONE'),
        ),
    ]

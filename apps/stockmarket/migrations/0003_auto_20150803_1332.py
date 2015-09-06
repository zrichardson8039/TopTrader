# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0002_auto_20150803_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='prices_url',
            field=models.CharField(default='NONE', max_length=256),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0005_auto_20150803_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='prices_url',
            field=models.CharField(max_length=256, blank=True, default=''),
        ),
    ]

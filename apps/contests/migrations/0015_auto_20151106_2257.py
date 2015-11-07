# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0014_auto_20151106_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='commission',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]

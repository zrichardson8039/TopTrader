# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0008_auto_20151105_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='net_income',
            field=models.DecimalField(max_digits=12, decimal_places=2),
        ),
    ]

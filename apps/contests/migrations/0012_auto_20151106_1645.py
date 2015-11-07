# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0011_auto_20151105_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='won',
        ),
        migrations.AddField(
            model_name='game',
            name='buys',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='buys_proceeds',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='commissions',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='sells',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='sells_proceeds',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]

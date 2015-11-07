# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0012_auto_20151106_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='buys',
        ),
        migrations.RemoveField(
            model_name='game',
            name='buys_proceeds',
        ),
        migrations.RemoveField(
            model_name='game',
            name='commissions',
        ),
        migrations.RemoveField(
            model_name='game',
            name='sells',
        ),
        migrations.RemoveField(
            model_name='game',
            name='sells_proceeds',
        ),
        migrations.AddField(
            model_name='game',
            name='cash',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=100000),
        ),
        migrations.AddField(
            model_name='game',
            name='margin',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='stock',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='total_return',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='net_income',
            field=models.DecimalField(decimal_places=2, max_digits=12, default=0),
        ),
    ]

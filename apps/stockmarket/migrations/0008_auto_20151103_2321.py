# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0007_stock_has_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='price',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='price',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='modified_at',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0005_auto_20151103_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

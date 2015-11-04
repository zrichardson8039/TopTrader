# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20151103_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]

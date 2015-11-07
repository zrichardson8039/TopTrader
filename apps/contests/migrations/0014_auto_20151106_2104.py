# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0013_auto_20151106_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='total_return',
            new_name='total_value',
        ),
    ]

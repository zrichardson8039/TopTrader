# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0007_auto_20151104_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='won',
            field=models.BooleanField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0003_auto_20150803_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(unique=True, max_digits=8, decimal_places=2, default=0),
        ),
    ]

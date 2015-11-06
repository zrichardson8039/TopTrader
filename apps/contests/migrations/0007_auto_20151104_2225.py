# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20151104_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=2, choices=[('BO', 'BUY-TO-OPEN'), ('BC', 'BUY-TO-CLOSE'), ('SO', 'SELL-TO-OPEN'), ('SC', 'SELL-TO-CLOSE')]),
        ),
    ]

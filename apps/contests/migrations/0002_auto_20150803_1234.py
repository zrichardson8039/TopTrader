# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=2, default='H', choices=[('BO', 'BUY-TO-OPEN'), ('BC', 'BUY-TO-CLOSE'), ('SO', 'SELL-TO-OPEN'), ('SC', 'SELL-TO-CLOSE'), ('H', 'HOLD')]),
        ),
    ]

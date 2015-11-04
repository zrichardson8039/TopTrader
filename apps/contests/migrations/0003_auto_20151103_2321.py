# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_auto_20150803_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='game',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='game',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='record',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='record',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='record',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='modified_at',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=2, choices=[('BO', 'BUY-TO-OPEN'), ('BC', 'BUY-TO-CLOSE'), ('SO', 'SELL-TO-OPEN'), ('SC', 'SELL-TO-CLOSE')], default='H'),
        ),
    ]

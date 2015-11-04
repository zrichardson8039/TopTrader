# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0004_auto_20151103_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='trader',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='contest',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='quote',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='contestant',
        ),
        migrations.RemoveField(
            model_name='game',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
        migrations.AddField(
            model_name='game',
            name='net_income',
            field=models.DecimalField(max_digits=12, default=0, decimal_places=2),
        ),
        migrations.AddField(
            model_name='game',
            name='trader',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='won',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]

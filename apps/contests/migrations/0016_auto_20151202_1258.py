# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0015_auto_20151106_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cash', models.DecimalField(max_digits=12, default=100000, decimal_places=2)),
                ('margin', models.DecimalField(max_digits=12, default=0, decimal_places=2)),
                ('shares', models.IntegerField(default=0)),
                ('stock_value', models.DecimalField(max_digits=12, default=0, decimal_places=2)),
                ('net_income', models.DecimalField(max_digits=12, default=0, decimal_places=2)),
                ('trader', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='trader',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='game',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]

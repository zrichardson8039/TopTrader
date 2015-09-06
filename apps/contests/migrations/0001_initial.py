# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockmarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('wins', models.IntegerField(default=0, null=True)),
                ('losses', models.IntegerField(default=0, null=True)),
                ('net_income', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('creator', models.ForeignKey(related_name='contests_record_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('trader', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('transaction_type', models.CharField(default=b'H', max_length=2, choices=[(b'BO', b'BUY-TO-OPEN'), (b'BC', b'BUY-TO-CLOSE'), (b'SO', b'SELL-TO-OPEN'), (b'SC', b'SELL-TO-CLOSE'), (b'H', b'HOLD')])),
                ('shares', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(to='contests.Game')),
                ('creator', models.ForeignKey(related_name='contests_transaction_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('quote', models.ForeignKey(default=0, to='stockmarket.Price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='contestant',
            field=models.ForeignKey(related_name='contestant', to='contests.Record'),
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(related_name='contests_game_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='opponent',
            field=models.ForeignKey(related_name='opponent', to='contests.Record'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(related_name='winner', to='contests.Record'),
        ),
    ]

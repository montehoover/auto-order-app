# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amazonid', models.CharField(max_length=200)),
                ('frequency_qty', models.IntegerField(default=1)),
                ('frequency_unit', models.CharField(max_length=200, default='Month')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

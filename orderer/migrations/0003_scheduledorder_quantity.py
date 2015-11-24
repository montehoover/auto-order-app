# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderer', '0002_auto_20151123_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledorder',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

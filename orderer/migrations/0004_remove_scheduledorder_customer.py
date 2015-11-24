# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderer', '0003_scheduledorder_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledorder',
            name='customer',
        ),
    ]

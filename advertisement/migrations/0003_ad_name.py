# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20170215_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='name',
            field=models.CharField(default='dummy1', max_length=255),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170326_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='link',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]

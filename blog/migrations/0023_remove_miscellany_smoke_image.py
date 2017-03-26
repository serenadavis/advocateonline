# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20170326_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='smoke_image',
        ),
    ]

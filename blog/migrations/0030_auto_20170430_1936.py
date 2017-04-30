# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20170329_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='smoke_image',
        ),
        migrations.RemoveField(
            model_name='miscellany',
            name='votes',
        ),
    ]

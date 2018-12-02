# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20180222_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='issue',
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]

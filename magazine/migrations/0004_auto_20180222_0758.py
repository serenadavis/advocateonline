# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20180222_0752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banners',
            new_name='Banner',
        ),
    ]

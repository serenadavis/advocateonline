# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_miscpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MiscPost',
        ),
    ]

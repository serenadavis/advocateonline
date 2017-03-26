# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170325_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miscellany',
            old_name='model_image',
            new_name='image',
        ),
    ]

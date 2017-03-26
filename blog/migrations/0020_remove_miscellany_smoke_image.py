# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170326_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='smoke_image',
        ),
    ]

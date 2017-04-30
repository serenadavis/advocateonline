# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20170326_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='link',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]

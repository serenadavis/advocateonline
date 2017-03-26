# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170325_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='image',
        ),
        migrations.AddField(
            model_name='miscellany',
            name='model_image',
            field=models.ImageField(null=True, upload_to=blog.models.upload_image_to, blank=True),
        ),
    ]

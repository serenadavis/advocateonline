# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20170326_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='image',
            field=models.ImageField(null=True, upload_to=blog.models.upload_image_to, blank=True),
        ),
    ]

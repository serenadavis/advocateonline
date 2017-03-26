# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20170326_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='image',
            field=models.ImageField(default=b'smoke_small.png', null=True, upload_to=blog.models.upload_image_to, blank=True),
        ),
    ]

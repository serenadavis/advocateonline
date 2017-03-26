# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170326_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='smoke_image',
            field=models.ImageField(default=b'media/smoke_small.png', upload_to=blog.models.upload_image_to),
        ),
    ]

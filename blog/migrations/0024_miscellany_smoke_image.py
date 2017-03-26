# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_miscellany_smoke_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscellany',
            name='smoke_image',
            field=models.ImageField(default=b'smoke_small.png', upload_to=blog.models.upload_image_to),
        ),
    ]

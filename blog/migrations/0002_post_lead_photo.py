# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lead_photo',
            field=models.ImageField(null=True, upload_to=blog.models.upload_image_to, blank=True),
            preserve_default=True,
        ),
    ]

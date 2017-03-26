# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170226_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscellany',
            name='image',
            field=models.ImageField(null=True, upload_to=blog.models.upload_image_to, blank=True),
        ),
    ]

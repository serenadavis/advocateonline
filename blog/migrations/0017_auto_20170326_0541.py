# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_miscellany_smoke_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='smoke_image',
            field=models.ImageField(default=b'magazine/static/magazine/images/smoke_small.png', upload_to=blog.models.upload_image_to),
        ),
    ]

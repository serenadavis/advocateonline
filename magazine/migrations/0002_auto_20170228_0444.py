# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(null=True, upload_to=magazine.models.upload_image_to, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(upload_to=magazine.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='issue',
            name='cover_image',
            field=versatileimagefield.fields.VersatileImageField(null=True, upload_to=magazine.models.issue_upload_to, blank=True),
        ),
    ]

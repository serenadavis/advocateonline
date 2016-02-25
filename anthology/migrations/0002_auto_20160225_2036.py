# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import anthology.models


class Migration(migrations.Migration):

    dependencies = [
        ('anthology', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='first_image',
        ),
        migrations.AddField(
            model_name='content',
            name='lead_photo',
            field=models.ImageField(null=True, upload_to=anthology.models.upload_image_to, blank=True),
        ),
        migrations.AlterField(
            model_name='decade',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=anthology.models.upload_image_to, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170326_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smoke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.upload_image_to, blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_lead_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=select2.fields.ManyToManyField(default=None, to='blog.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=select2.fields.ManyToManyField(default=None, to='blog.Tag', blank=True),
        ),
    ]

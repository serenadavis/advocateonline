# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import advertisement.models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_ad_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='image_src',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='url_redirect',
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(default=datetime.datetime(2017, 2, 18, 6, 2, 15, 742995, tzinfo=utc), upload_to=advertisement.models.issue_upload_to),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0006_ad_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.CharField(default=b'home', max_length=255, choices=[(b'home', b'Homepage'), (b'blog', b'Blog'), (b'poetry', b'Poetry'), (b'art', b'Art'), (b'features', b'Features'), (b'columns', b'Columns'), (b'notes', b'Notes')]),
        ),
    ]

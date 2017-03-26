# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_miscellany_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscellany',
            name='link',
            field=models.TextField(max_length=255, null=True),
        ),
    ]

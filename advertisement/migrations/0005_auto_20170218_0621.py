# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_auto_20170218_0602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='upload_date',
            new_name='date_added',
        ),
    ]

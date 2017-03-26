# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_miscellany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

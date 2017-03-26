# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_delete_smoke'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscellany',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

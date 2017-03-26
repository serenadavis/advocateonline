# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170326_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='miscellany',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='miscellany',
            name='vote_score',
        ),
        migrations.AddField(
            model_name='miscellany',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

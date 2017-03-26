# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_miscellany_smoke_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellany',
            name='votes',
        ),
        migrations.AddField(
            model_name='miscellany',
            name='num_vote_down',
            field=models.PositiveIntegerField(default=0, db_index=True),
        ),
        migrations.AddField(
            model_name='miscellany',
            name='num_vote_up',
            field=models.PositiveIntegerField(default=0, db_index=True),
        ),
        migrations.AddField(
            model_name='miscellany',
            name='vote_score',
            field=models.IntegerField(default=0, db_index=True),
        ),
    ]

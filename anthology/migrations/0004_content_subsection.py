# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anthology', '0003_auto_20161107_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='subsection',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

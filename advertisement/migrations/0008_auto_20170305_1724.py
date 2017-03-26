# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0007_auto_20170225_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.CharField(default=b'home', max_length=255, choices=[(b'home', b'Homepage'), (b'blog', b'Blog'), (b'poetry', b'Poetry'), (b'fiction', b'Fiction'), (b'art', b'Art'), (b'features', b'Features'), (b'columns', b'Columns'), (b'notes', b'Notes')]),
        ),
    ]

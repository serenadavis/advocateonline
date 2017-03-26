# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_miscellany_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellany',
            name='image',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/'),
        ),
    ]

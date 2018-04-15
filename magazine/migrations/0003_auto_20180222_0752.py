# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20170228_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', versatileimagefield.fields.VersatileImageField(upload_to=magazine.models.upload_image_to)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=magazine.models.issue_upload_to, blank=True),
        ),
        migrations.AddField(
            model_name='banners',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
        ),
    ]

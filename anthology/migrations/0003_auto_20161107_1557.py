# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields
import anthology.models
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('anthology', '0002_auto_20160225_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('intro', redactor.fields.RedactorField(verbose_name='Text')),
                ('number', models.IntegerField()),
                ('cover_image', models.ImageField(null=True, upload_to=anthology.models.upload_image_to, blank=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='decade',
        ),
        migrations.DeleteModel(
            name='Decade',
        ),
        migrations.AddField(
            model_name='content',
            name='path',
            field=select2.fields.ForeignKey(default=None, to='anthology.Path'),
        ),
    ]

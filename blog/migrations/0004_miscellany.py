# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160225_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miscellany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body_text', models.TextField(max_length=255)),
                ('pub_date', models.DateField()),
                ('nickname', models.CharField(max_length=10)),
            ],
        ),
    ]

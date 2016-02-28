# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=100)),
                ('body', redactor.fields.RedactorField(verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('authors', select2.fields.ManyToManyField(to='anthology.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('intro', redactor.fields.RedactorField(verbose_name='Text')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=1000, blank=True)),
                ('caption', models.TextField(max_length=10000, blank=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='decade',
            name='cover_image',
            field=models.ForeignKey(default=None, blank=True, to='anthology.Images', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='decade',
            field=select2.fields.ForeignKey(to='anthology.Decade'),
        ),
        migrations.AddField(
            model_name='content',
            name='first_image',
            field=models.ForeignKey(default=None, blank=True, to='anthology.Images', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='posted',
            field=select2.fields.ManyToManyField(to='anthology.Category'),
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=select2.fields.ManyToManyField(to='anthology.Tag'),
        ),
    ]

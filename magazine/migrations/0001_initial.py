# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import magazine.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('publishDate', models.DateTimeField(default=datetime.datetime.now)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('teaser', tinymce.models.HTMLField(blank=True)),
                ('body', tinymce.models.HTMLField(blank=True)),
                ('medium', tinymce.models.HTMLField(blank=True)),
                ('size', tinymce.models.HTMLField(blank=True)),
                ('statement', tinymce.models.HTMLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='magazine.Content')),
                ('photo', models.ImageField(null=True, upload_to=magazine.models.upload_image_to, blank=True)),
            ],
            options={
            },
            bases=('magazine.content',),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('streetAddress1', models.CharField(max_length=255)),
                ('streetAddress2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=255)),
                ('customerID', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='magazine.Content')),
                ('photo', models.ImageField(upload_to=magazine.models.upload_image_to)),
            ],
            options={
            },
            bases=('magazine.content',),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('theme', models.CharField(max_length=255, null=True, blank=True)),
                ('cover_image', models.ImageField(null=True, upload_to=magazine.models.issue_upload_to, blank=True)),
                ('issue', models.CharField(default=b'Fall', max_length=255, choices=[(b'Fall', b'Fall'), (b'Winter', b'Winter'), (b'Spring', b'Spring'), (b'Commencement', b'Commencement')])),
                ('year', models.IntegerField(null=True, blank=True)),
                ('pub_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('streetAddress1', models.CharField(max_length=255)),
                ('streetAddress2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=255)),
                ('customerID', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('purchases_json', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('streetAddress1', models.CharField(max_length=255)),
                ('streetAddress2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=255)),
                ('customerID', models.CharField(max_length=255)),
                ('renew', models.BooleanField(default=False)),
                ('subscriptionType', models.CharField(max_length=255, choices=[(b'Three year; US', b'Three year; US'), (b'Two year; US', b'Two year; US'), (b'One year; US', b'One year; US'), (b'Three year; non-US', b'Three year; non-US'), (b'Two year; non-US', b'Two year; non-US'), (b'One year; non-US', b'One year; non-US')])),
                ('time', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='contributors',
            field=models.ManyToManyField(to='magazine.Contributor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(related_name='section', to='magazine.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(to='magazine.Tag', blank=True),
            preserve_default=True,
        ),
    ]

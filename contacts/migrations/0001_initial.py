# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=255, verbose_name=b'First name')),
                ('middleName', models.CharField(max_length=255, verbose_name=b'Middle name', blank=True)),
                ('lastName', models.CharField(max_length=255, verbose_name=b'Last name', blank=True)),
                ('article', models.CharField(max_length=255, verbose_name=b'Article', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title', blank=True)),
                ('nickName', models.CharField(max_length=255, verbose_name=b'Nickname', blank=True)),
                ('streetAddress1', models.CharField(max_length=255, verbose_name=b'Address 1', blank=True)),
                ('streetAddress2', models.CharField(max_length=255, verbose_name=b'Address 2', blank=True)),
                ('streetAddress3', models.CharField(max_length=255, verbose_name=b'Address 3', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name=b'City', blank=True)),
                ('state', models.CharField(max_length=255, verbose_name=b'State', blank=True)),
                ('zipCode', models.CharField(max_length=255, verbose_name=b'Zip code', blank=True)),
                ('country', models.CharField(max_length=255, verbose_name=b'Country', blank=True)),
                ('email1', models.CharField(max_length=255, verbose_name=b'Email', blank=True)),
                ('email2', models.CharField(max_length=255, verbose_name=b'Email 2', blank=True)),
                ('phone', models.CharField(max_length=255, verbose_name=b'Phone', blank=True)),
                ('linkedIn', models.CharField(max_length=255, verbose_name=b'LinkedIn', blank=True)),
                ('twitter', models.CharField(max_length=255, verbose_name=b'Twitter', blank=True)),
                ('facebook', models.CharField(max_length=255, verbose_name=b'Facebook', blank=True)),
                ('followed', models.BooleanField(default=False, verbose_name=b'Followed?')),
                ('website', models.CharField(max_length=255, verbose_name=b'Website', blank=True)),
                ('profession', models.CharField(max_length=255, verbose_name=b'Profession', blank=True)),
                ('graduationYear', models.CharField(max_length=255, verbose_name=b'Graduation year', blank=True)),
                ('otherDegrees', models.CharField(max_length=255, verbose_name=b'Other degrees', blank=True)),
                ('board', models.CharField(max_length=255, verbose_name=b'Board', blank=True)),
                ('positionHeld', models.CharField(max_length=255, verbose_name=b'Position held', blank=True)),
                ('publishedWork', models.TextField(verbose_name=b'Published work', blank=True)),
                ('notes', models.TextField(verbose_name=b'Notes', blank=True)),
                ('donationBracket', models.CharField(max_length=255, verbose_name=b'Donation bracket', blank=True)),
                ('tier', models.CharField(max_length=255, verbose_name=b'Tier', blank=True)),
                ('formCategory', models.CharField(max_length=255, verbose_name=b'Form category', blank=True)),
                ('dateAdded', models.DateField(auto_now_add=True, verbose_name=b'Date added')),
            ],
            options={
                'ordering': ('firstName', 'lastName'),
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('category', models.IntegerField(default=0, choices=[(0, b'Other'), (1, b'Phone call'), (2, b'Email'), (3, b'Donation'), (4, b'Purchase'), (5, b'Subscription Start'), (6, b'Subscription End')])),
                ('donationAmount', models.IntegerField(null=True, verbose_name=b'Donation amount (if applicable)', blank=True)),
                ('note', models.TextField()),
                ('contact', models.ForeignKey(to='contacts.Contact')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([('firstName', 'lastName')]),
        ),
    ]

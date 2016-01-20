from django.db import models
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.encoding import smart_unicode, smart_str
from tinymce import models as tinymce_models
from bs4 import BeautifulSoup
import re

import os
import datetime

# Create your models here.

# class Section(models.Model):
#     name = models.CharField(max_length=255, unique=True)

#     def __unicode__(self):
#         return self.name

# class Contributor(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, unique=True)

#     def __unicode__(self):
#       return self.name
#     def slug(self):
#       return self.name.replace(" ", "_")
#     def get_absolute_url(self):
#      # Can't use .format because name is not always
#      return '/contributor/' +  str(self.id) + '/' +  self.slug()
#      # return '/contributor/{0}/{1}'.format(self.id, self.slug())

# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=100)

#     def __unicode__(self):
#         return self.name

class Decade(models.Model):
	name = models.CharField(max_length=255)

# class ContentQuerySet(models.query.QuerySet):
#     def published(self):
#         return self.filter(Q(publishDate__lte=datetime.datetime.now()) | Q(publishDate__isnull=True))

# class ContentManager(models.Manager):
#     def get_queryset(self):
#         return ContentQuerySet(self.model, using=self._db)

#     def published(self):
#         return self.get_queryset().published()

# class Content(models.Model):
#     objects = ContentManager()
#     title = models.CharField(max_length=255)
#     publishDate = models.DateTimeField(default=datetime.datetime.now)
#     subtitle = models.CharField(max_length=255, blank=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     teaser = tinymce_models.HTMLField(blank=True)
#     body = tinymce_models.HTMLField(blank=True)

#     # Legacy fields; we should probably get rid of this eventually
#     medium = tinymce_models.HTMLField(blank=True)
#     size = tinymce_models.HTMLField(blank=True)
#     statement = tinymce_models.HTMLField(blank=True)

#     issue = models.ForeignKey('Issue')
#     section = models.ForeignKey('Section', related_name="section")
#     contributors = models.ManyToManyField(Contributor)
#     tags = models.ManyToManyField(Tag, blank=True)

#     def __unicode__(self):
#         return self.title

#     def get_absolute_url(self):
#         return '/content/{0}/'.format(self.id)

#     def description(self):
#         txt = ' '.join(BeautifulSoup(self.teaser).findAll(text=True))
#         return txt
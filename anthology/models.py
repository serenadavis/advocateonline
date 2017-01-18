from django.db import models
import tinymce
from bs4 import BeautifulSoup
import re
from redactor.fields import RedactorField
import select2.fields

import os
import datetime


def upload_image_to(instance, filename):
    fname = ''.join([c for c in filename if c.isalnum() or c == '.'])
    return os.path.join('sites', 'default', 'files', fname)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        # Can't use .format because name is not always
        return '/anthology/tag/' +  str(self.slug)
        # return '/contributor/{0}/{1}'.format(self.id, self.slug())

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        # Can't use .format because name is not always
        return '/anthology/contributor/' +  str(self.id)
        # return '/contributor/{0}/{1}'.format(self.id, self.slug())

class Images(models.Model):
    path = models.CharField(max_length=1000, blank=True)
    caption = models.TextField(max_length=10000, blank=True)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return unicode(self.id)
    def get_absolute_url(self):
        return "/media/" + path


class Theme(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100)
    def __unicode__(self):
        return self.name

class Path(models.Model):
    name = models.CharField(max_length=255)
    intro = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='tmp/',
        allow_file_upload=True,
        allow_image_upload=True
    )
    number = models.IntegerField()
    cover_image = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    slug = models.SlugField(max_length=100)
    def get_image(self):
        if self.cover_image:
            return self.cover_image.url
        else:
            return ""
    def __unicode__(self):
        return self.name

# Create your models here.
class Content(models.Model):
    subsection = models.IntegerField()
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    body = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='tmp/',
        allow_file_upload=True,
        allow_image_upload=True
    )
    created = models.DateTimeField(auto_now_add=True)
    tags = select2.fields.ManyToManyField(Tag)
    posted = select2.fields.ManyToManyField(Category)
    authors = select2.fields.ManyToManyField(Author)
    path = select2.fields.ForeignKey(Path, default=None)
    lead_photo = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/anthology/content/'+ self.slug
    def crop_first_image(self):
        return self.lead_photo
    def teaser(self):
        txt = re.sub("\{\{.*\}\}","",BeautifulSoup(self.body).text)
        i = 400
        while len(txt) > i and txt[i-1] != ".":
            i += 1
        if "(function" in txt:
            if txt.index("(function") < i:
                i = txt.index("(function") 
        return txt[:i]


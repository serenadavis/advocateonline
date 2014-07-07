import os
import datetime

from django.db import models
from django.utils.text import slugify

import tinymce


def now():
    now = int((datetime.datetime.utcnow() -
                datetime.datetime(2014, 1, 1)).total_seconds() * 10 ** 6)
    return unicode(now)

def issue_upload_to(instance, filename):
    fname = ''.join([c for c in filename if c.isalnum() or c == '.'])
    return os.path.join('issue_covers', str(instance.pub_date.year), 
            slugify(instance.name), now() + '_' + fname)

class Issue(models.Model):
    name = models.CharField(max_length=255, unique=True)
    pub_date = models.DateField()
    cover_image = models.ImageField(upload_to=issue_upload_to, blank=True,
            null=True)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    
    def __unicode__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    teaser = models.TextField()
    body = tinymce.models.HTMLField()

    # Legacy fields; we should probably get rid of this eventually
    medium = tinymce.models.HTMLField()
    size = tinymce.models.HTMLField()
    statement = tinymce.models.HTMLField()

    issue = models.ForeignKey('Issue')
    section = models.ForeignKey('Section')
    contributors = models.ManyToManyField(Contributor)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title


class Article(Content):
    pass


def upload_image_to(instance, filename):
    fname = ''.join([c for c in filename if c.isalnum() or c == '.'])

    return os.path.join('images', slugify(instance.issue.name), 
            now() + '_' + fname)


class Image(Content):
    photo = models.ImageField(upload_to=upload_image_to)



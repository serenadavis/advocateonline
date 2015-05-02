from django.db import models
import tinymce
from bs4 import BeautifulSoup
import re

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        # Can't use .format because name is not always
        return '/blog/tag/' +  str(self.slug)
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
        return '/blog/contributor/' +  str(self.id)
        # return '/contributor/{0}/{1}'.format(self.id, self.slug())

class Images(models.Model):
    path = models.CharField(max_length=1000, blank=True)
    caption = models.TextField(max_length=10000, blank=True)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return self.id
    def get_absolute_url(self):
        return "/media/" + path


class Theme(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100)
    def __unicode__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    body = tinymce.models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    posted = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    theme = models.ForeignKey(Theme)
    first_image = models.ForeignKey(Images,null=True, blank=True, default = None)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/blog/post/'+ self.slug
    def teaser(self):
        txt = re.sub("\{\{.*\}\}","",BeautifulSoup(self.body).text)
        i = 350
        while len(txt) > i and txt[i-1] != ".":
            i += 1
        return txt[:i]


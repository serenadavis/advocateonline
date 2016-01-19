from django.db import models
import tinymce
from bs4 import BeautifulSoup
import re
from redactor.fields import RedactorField
import select2.fields

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
    theme = select2.fields.ForeignKey(Theme)
    first_image = models.ForeignKey(Images,null=True, blank=True, default = None)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/blog/post/'+ self.slug
    def crop_first_image(self):
        return self.first_image
    def teaser(self):
        txt = re.sub("\{\{.*\}\}","",BeautifulSoup(self.body).text)
        i = 800
        while len(txt) > i and txt[i-1] != ".":
            i += 1
        if "(function" in txt:
            if txt.index("(function") < i:
                i = txt.index("(function") 
        return txt[:i]



from django.db import models
import tinymce

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    
    def __unicode__(self):
        return self.name

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
        
class Images(models.Model):
    path = models.CharField(max_length=1000, blank=True)
    caption = models.CharField(max_length=10000, blank=True)
    slug = models.SlugField(max_length=100)
    
    def __unicode__(self):
        return self.id


class Theme(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    body = tinymce.models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    posted = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    theme = models.ForeignKey(Theme)

    def __unicode__(self):
        return self.title
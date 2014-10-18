from django.db import models

# Create your models here.
class Post(models.Model):
	post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    body = models.TextField()
    image = models.ImageField()
    music=  models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    authors = models.TextField()

    def __unicode__(self):
        return self.title

class Tag (models.Model):
	url = models.URLField()


### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
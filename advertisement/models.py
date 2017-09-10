from django.db import models
import datetime
import os


def now():
    now = int((datetime.datetime.utcnow() -
                datetime.datetime(2014, 1, 1)).total_seconds() * 10 ** 6)
    return unicode(now)

# issue_covers/issue.year/filename.jpg
def issue_upload_to(instance, filename):
    fname = ''.join([c for c in filename if c.isalnum() or c == '.'])
    return os.path.join('ads', now() + '_' + fname)

class Ad(models.Model):

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=issue_upload_to)
    date_added = models.DateTimeField(default=datetime.datetime.now)

    LOCATIONS = (
        ('home', 'Homepage'),
        ('blog', 'Blog'),
        ('poetry', 'Poetry'),
        ('fiction', 'Fiction'),
        ('art', 'Art'),
        ('features', 'Features'),
        ('columns', 'Columns'),
        ('notes', 'Notes'),
    )

    location = models.CharField(max_length=255, choices=LOCATIONS, default='home')
    enabled = models.BooleanField(default=True)


    def __unicode__(self):
        return self.name

import os
import datetime

from django.db import models
from django.utils.text import slugify

import tinymce


class Donation(models.Model):

    amount = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    streetAddress1 = models.CharField(max_length=255)
    streetAddress2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)    
    state = models.CharField(max_length=255)    
    country = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    customerID = models.CharField(max_length=255) 
    time = models.CharField(max_length=255)


class Subscriber(models.Model):

    SUBSCRIPTION_CHOICES = (
        ('Three year; US', 'Three year; US'),
        ('Two year; US', 'Two year; US'),
        ('One year; US', 'One year; US'),
        ('Three year; non-US', 'Three year; non-US'),
        ('Two year; non-US', 'Two year; non-US'),
        ('One year; non-US', 'One year; non-US')
    )

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    streetAddress1 = models.CharField(max_length=255)
    streetAddress2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)    
    state = models.CharField(max_length=255)    
    country = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    customerID = models.CharField(max_length=255) 
    renew = models.BooleanField()
    subscriptionType = models.CharField(max_length=255, choices=SUBSCRIPTION_CHOICES)
    time = models.CharField(max_length=255)


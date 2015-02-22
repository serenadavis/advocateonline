from django.db import models

# Create your models here.
class Contact(models.Model):
	firstName = models.CharField(max_length=255) 
	lastName = models.CharField(max_length=255)
	middleName = models.CharField(max_length=255, blank=True)
	title = models.CharField(max_length=255)
	nickName = models.CharField(max_length=255, blank=True)
	streetAddress1 = models.CharField(max_length=255)
	streetAddress2 = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	zipCode = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	profession = models.CharField(max_length=255, blank=True)
	graduationYear = models.CharField(max_length=255)
	degrees = models.CharField(max_length=255, blank=True)
	board = models.CharField(max_length=255, blank=True)
	positionHeld = models.CharField(max_length=255, blank=True)
	publishedWork = models.TextField(blank=True)


class Interaction(models.Model):
	INTERACTION_CATEGORIES = ((0, 'Other'),
							  (1, 'Phone call'),
							  (2, 'Email'),
							  (3, 'Donation'),
							  (4, 'Purchase'),
							  (5, 'Subscription Start'),
							  (6, 'Subscription End'))

	contact = models.ForeignKey(Contact)
	date = models.DateField()
	category = models.IntegerField(choices=INTERACTION_CATEGORIES, default=0)
	note = models.TextField()

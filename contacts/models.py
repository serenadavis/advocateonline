from django.db import models

# Create your models here.
class Contact(models.Model):
	def __unicode__(self):
		return self.article + " " + self.firstName + " " + self.lastName + " " + self.title

	def fullName(self):
		return self.article + " " + self.firstName + " " + self.lastName + " " + self.title

	firstName = models.CharField(max_length=255) 
	lastName = models.CharField(max_length=255, blank=True)
	middleName = models.CharField(max_length=255, blank=True)
	article = models.CharField(max_length=255, blank=True)
	title = models.CharField(max_length=255, blank=True)
	nickName = models.CharField(max_length=255, blank=True)
	streetAddress1 = models.CharField(max_length=255)
	streetAddress2 = models.CharField(max_length=255, blank=True)
	streetAddress3 = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	zipCode = models.CharField(max_length=255)
	country = models.CharField(max_length=255, blank=True)
	email1 = models.CharField(max_length=255, blank=True)
	email2 = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=255, blank=True)
	linkedIn = models.CharField(max_length=255, blank=True)
	twitter = models.CharField(max_length=255, blank=True)
	facebook = models.CharField(max_length=255, blank=True)
	followed = models.BooleanField(default=False)
	website = models.CharField(max_length=255, blank=True)
	profession = models.CharField(max_length=255, blank=True)
	graduationYear = models.CharField(max_length=255, blank=True)
	otherDegrees = models.CharField(max_length=255, blank=True)
	board = models.CharField(max_length=255, blank=True)
	positionHeld = models.CharField(max_length=255, blank=True)
	publishedWork = models.TextField(blank=True)
	notes = models.TextField(blank=True)
	donationBracket = models.CharField(max_length=255, blank=True)
	#donationYears = 
	#donatedAmount = 
	#lastContact = 
	tier = models.CharField(max_length=255, blank=True)
	formCategory = models.CharField(max_length=255, blank=True)
	dateAdded = models.DateField(auto_now_add=True, blank=True)


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

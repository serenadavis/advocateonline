from django.db import models

# class Board(models.Model):
# 	name = models.CharField(max_length=255)

# Create your models here.
class Contact(models.Model):
	def full_name(self):
		return self.article + " " + self.firstName + " " + self.lastName + " " + self.title

	def __unicode__(self):
		return self.full_name()

	def full_address(self):
		return self.streetAddress1 + '\n' + self.streetAddress2 + '\n' + self.streetAddress3

	class Meta:
		ordering = ('firstName', 'lastName') # default sort order
		unique_together = ['firstName', 'lastName'] # no two contacts can have the same first/last name

	firstName = models.CharField(max_length=255, verbose_name='First name') 
	middleName = models.CharField(max_length=255, blank=True, verbose_name='Middle name')
	lastName = models.CharField(max_length=255, blank=True, verbose_name='Last name')
	article = models.CharField(max_length=255, blank=True, verbose_name='Article')
	title = models.CharField(max_length=255, blank=True, verbose_name='Title')
	nickName = models.CharField(max_length=255, blank=True, verbose_name='Nickname')
	streetAddress1 = models.CharField(max_length=255, blank=True, verbose_name='Address 1')
	streetAddress2 = models.CharField(max_length=255, blank=True, verbose_name='Address 2')
	streetAddress3 = models.CharField(max_length=255, blank=True, verbose_name='Address 3')
	city = models.CharField(max_length=255, blank=True, verbose_name='City')
	state = models.CharField(max_length=255, blank=True, verbose_name='State')
	zipCode = models.CharField(max_length=255, blank=True, verbose_name='Zip code')
	country = models.CharField(max_length=255, blank=True, verbose_name='Country')
	email1 = models.CharField(max_length=255, blank=True, verbose_name='Email')
	email2 = models.CharField(max_length=255, blank=True, verbose_name='Email 2')
	phone = models.CharField(max_length=255, blank=True, verbose_name='Phone')
	linkedIn = models.CharField(max_length=255, blank=True, verbose_name='LinkedIn')
	twitter = models.CharField(max_length=255, blank=True, verbose_name='Twitter')
	facebook = models.CharField(max_length=255, blank=True, verbose_name='Facebook')
	followed = models.BooleanField(default=False, verbose_name='Followed?')
	website = models.CharField(max_length=255, blank=True, verbose_name='Website')
	profession = models.CharField(max_length=255, blank=True, verbose_name='Profession')
	graduationYear = models.CharField(max_length=255, blank=True, verbose_name='Graduation year')
	otherDegrees = models.CharField(max_length=255, blank=True, verbose_name='Other degrees')
	board = models.CharField(max_length=255, blank=True, verbose_name='Board')
	positionHeld = models.CharField(max_length=255, blank=True, verbose_name='Position held')
	publishedWork = models.TextField(blank=True, verbose_name='Published work')
	notes = models.TextField(blank=True, verbose_name='Notes')
	donationBracket = models.CharField(max_length=255, blank=True, verbose_name='Donation bracket')
	#donationYears = 
	#donatedAmount = 
	#lastContact = 
	tier = models.CharField(max_length=255, blank=True, verbose_name='Tier')
	formCategory = models.CharField(max_length=255, blank=True, verbose_name='Form category')
	dateAdded = models.DateField(auto_now_add=True, blank=True, verbose_name='Date added')


class Interaction(models.Model):
	def __unicode__(self):
		return str(self.date) + ': ' + self.note

	INTERACTION_CATEGORIES = ((0, 'Other'),
							  (1, 'Phone call'),
							  (2, 'Email'),
							  (3, 'Donation'),
							  (4, 'Purchase'),
							  (5, 'Subscription Start'),
							  (6, 'Subscription End'))

	contact = models.ForeignKey(Contact)
	date = models.DateField(null=True, blank=True)
	category = models.IntegerField(choices=INTERACTION_CATEGORIES, default=0)
	donationAmount = models.IntegerField(null=True, blank=True, verbose_name='Donation amount (if applicable)')
	note = models.TextField()

from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
	list_display = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'streetAddress1', 'city',
					'state', 'zipCode', 'email1', 'dateAdded')
	list_filter = ['state', 'graduationYear', 'tier', 'article', 'followed']
	search_fields = ['firstName', 'middleName', 'lastName', 'nickName']

# Register your models here.
admin.site.register(Contact, ContactAdmin)
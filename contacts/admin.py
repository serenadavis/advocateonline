from django.contrib import admin
from .models import *

class InteractionInline(admin.TabularInline):
	model = Interaction
	extra = 0

class ContactAdmin(admin.ModelAdmin):
	list_display = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'full_address', 'city',
					'state', 'zipCode', 'email1', 'dateAdded')
	list_filter = ['state', 'graduationYear', 'board', 'positionHeld', 'tier', 'article', 'followed', 'formCategory']
	search_fields = ['firstName', 'middleName', 'lastName', 'nickName']
	inlines = [InteractionInline]

class InteractionAdmin(admin.ModelAdmin):
	list_filter = ['category']

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Interaction, InteractionAdmin)
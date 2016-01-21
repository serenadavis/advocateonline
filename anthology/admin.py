from django.contrib import admin
from models import *


class DecadeAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Decade, DecadeAdmin)
from django.contrib import admin
from models import *
from mce_filebrowser.admin import MCEFilebrowserAdmin


class ContentAdmin(MCEFilebrowserAdmin):
    search_fields = ['tags']


class DecadeAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Decade, DecadeAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Theme)

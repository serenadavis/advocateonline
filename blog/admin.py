from django.contrib import admin
from .models import *
from mce_filebrowser.admin import MCEFilebrowserAdmin

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(Post,MyModelAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Theme)
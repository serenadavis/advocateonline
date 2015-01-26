from django.contrib import admin
from .models import *
from .forms import ContentForm

admin.site.register(Issue)
admin.site.register(Section)
admin.site.register(Contributor)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)

class ContentAdmin(admin.ModelAdmin):
    form = ContentForm
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('contributors', 'tags')

    
admin.site.register(Article, ContentAdmin)
admin.site.register(Image, ContentAdmin)
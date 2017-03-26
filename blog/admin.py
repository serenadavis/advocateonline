from django.contrib import admin
from .models import *
from .forms import BlogForm


class PostAdmin(admin.ModelAdmin):
	form = BlogForm
	search_fields = ['tags']

admin.site.register(Post, PostAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Theme)
admin.site.register(Miscellany)

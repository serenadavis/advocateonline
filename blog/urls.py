from django.conf.urls import patterns, include, url
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', "blog.views.main"),
    url(r'^post/(?P<slug>[a-zA-Z\d_\-]+)/$', 'blog.views.post'),
    # url(r'^theme', 'blog.views.theme'),
    url(r'^theme/(?P<theme_id>[\d]+)$', 'blog.views.individual_theme'),
    url(r'^contributor/(?P<author_id>[\d]+)$', 'blog.views.contributor_page'), 
    url(r'^category/(?P<category_id>[\d]+)$', 'blog.views.view_category'),
    url(r'^about', 'blog.views.about'),      
    url(r'^archives/$|^writing/$|^art/$|^multimedia/$', 'blog.views.sections'),
    url(r'^select2/', include('select2.urls')),
    # url(r'^writing', 'blog.views.writing'),
    # url(r'^multimedia', 'blog.views.multimedia'),
    # url(r'^themes', 'blog.views.themes')
)
from django.conf.urls import patterns, include, url
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url('', "blog.views.main"),
)
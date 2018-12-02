from django.conf.urls import include, url
from django.contrib import admin
import anthology.views
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', anthology.views.main),
]
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'magazine.views.index'),
    url(r'^article', 'magazine.views.index'),
    url(r'^issues$', 'magazine.views.issues'),
    url(r'^about$', 'magazine.views.masthead'),
    url(r'^issue/(?P<season>[a-zA-Z]+)-(?P<year>[\d]{4})/$', 'magazine.views.singleissue'),
    url(r'^donate$', 'magazine.views.donate'),
    url(r'^subscribe$', 'magazine.views.subscribe'),
    url(r'^submit$', 'magazine.views.submit'),
    url(r'^contact$', 'magazine.views.contact'),
    url(r'^alumni$', 'magazine.views.alumni'),
    url(r'^fiction|poetry|art|features$', 'magazine.views.sections'),
    url(r'^advertise$', 'magazine.views.advertise'),
    url(r'^150th$', 'magazine.views.onefifty'),
    url(r'^shop$', 'magazine.views.shop'),
    url(r'^comp$', 'magazine.views.comp'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    #url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
    url(r'^stripeSubmit$','magazine.views.stripeSubmit'),
    #http://stackoverflow.com/questions/901551/how-do-i-include-image-files-in-django-templates
    #http://stackoverflow.com/questions/19132123/name-settings-is-not-defined
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


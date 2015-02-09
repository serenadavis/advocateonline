from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'magazine.views.index'),
    url(r'^issues$', 'magazine.views.issues'),
    url(r'^about$', 'magazine.views.masthead'),
    url(r'^issue/(?P<season>[a-zA-Z]+)-(?P<year>[\d]{4})/$', 'magazine.views.singleissue'),
    url(r'^subscribe$', 'magazine.views.subscribe'),
    url(r'^submit$', 'magazine.views.submit'),
    url(r'^contact$', 'magazine.views.contact'),
    url(r'^alumni$', 'magazine.views.alumni'),
    url(r'^fiction/$|^poetry/$|^art/$|^features/$', 'magazine.views.sections'),
    url(r'^advertise$', 'magazine.views.advertise'),
    url(r'^150th$', 'magazine.views.onefifty'),
    url(r'^shop$', 'magazine.views.shop'),
    url(r'^comp$', 'magazine.views.comp'),
    url(r'^article/(?P<slug>[a-zA-Z\d_\-]+)/$', 'magazine.views.article'),
    # url(r'^search/q=?(?P<searchterm>[a-zA-Z\d_\-]+)/$', 'magazine.views.search'),
    url(r'^content/(?P<id>[\d]+)/$', 'magazine.views.content_piece'),
    url(r'^contributor/(?P<author_id>[\d]+)/(?P<name>.*)/$', 'magazine.views.contributor_page'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sendDonation$','payments.views.sendDonation'),

    url(r'^blog/', include('blog.urls')),
    url(r'^shopSubmit$','payments.views.shopSubmit'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    
    url(r'^donate$', 'payments.views.donate'),
    url(r'^stripeSubmit$','payments.views.stripeSubmit'),
    #http://stackoverflow.com/questions/901551/how-do-i-include-image-files-in-django-templates
    #http://stackoverflow.com/questions/19132123/name-settings-is-not-defined
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


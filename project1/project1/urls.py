from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app1.views.index'),
    url(r'^login/', 'app1.views._login'),
    url(r'^register/', 'app1.views.register'),
    url(r'^loginuser/', 'app1.views._loginuser'),
    url(r'^dashboard/', 'app1.views.dashboard'),
    url(r'^logout/', 'app1.views._logout'),
    
)



from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

from statisticum.games import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       (r'^games/', include('statisticum.games.urls')),
                       (r'^profiles/', include('statisticum.profiles.urls')),
                       (r'^accounts/',
                        include('registration.backends.simple.urls')),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$',
                             'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            )

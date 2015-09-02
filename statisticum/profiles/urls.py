from django.conf.urls import *
from django.conf import settings
from django.contrib.auth import views as auth_views

from statisticum.profiles.views import show
from statisticum.profiles.views import edit

urlpatterns = patterns('',
                       url(r'^show/(?P<id>\w+)$', show, name='profile_show'),
                       url(r'^edit/', edit, name='profile_edit'),
                       )

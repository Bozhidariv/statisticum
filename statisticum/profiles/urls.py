from django.conf.urls import *
from django.conf import settings
from django.contrib.auth import views as auth_views

from statisticum.profiles.views import index
from statisticum.profiles.views import add
from statisticum.profiles.views import edit

urlpatterns = patterns('',
	url(r'^$',index,name='games_index'),
    url(r'^add/$',add,name='profile_add'),
    url(r'^edit/(?P<id>\w+)/',edit,name='profile_edit'),
)

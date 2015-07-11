from django.conf.urls import *
from django.conf import settings
from django.contrib.auth import views as auth_views

from statisticum.games.views import index
from statisticum.games.views import show
from statisticum.games.views import add
from statisticum.games.views import edit
from statisticum.games.views import add_score
#from statisticum.games.views import preview
from statisticum.games.views import wins
from statisticum.games.views import losts
from statisticum.games.views import draws

urlpatterns = patterns('',
	url(r'^$',index,name='games_index'),
    url(r'^add/$',add,name='games_add'),
    url(r'^show/(?P<id>\w+)/',show,name='game_show'),
    url(r'^edit/(?P<id>\w+)/',edit,name='game_edit'),
    url(r'^add/score/(?P<id>\w+)/',add_score,name='game_add_score'),
    url(r'^wins/',wins,name='page_wins'),
    url(r'^losts/',losts,name='page_losts'),
    url(r'^draws/',draws,name='page_draws')
    #url(r'^new/preview/$',preview,name='game_preview'),
    

)

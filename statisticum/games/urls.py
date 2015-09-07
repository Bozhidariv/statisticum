from django.conf.urls import *
from django.conf import settings
from django.contrib.auth import views as auth_views

from statisticum.games.views import index
from statisticum.games.views import show
from statisticum.games.views import add
from statisticum.games.views import edit
from statisticum.games.views import add_score
from statisticum.games.views import wins
from statisticum.games.views import losts
from statisticum.games.views import draws
from statisticum.games.views import for_approval
from statisticum.games.views import edit_approval
from statisticum.games.views import rejected
from statisticum.games.views import show_rejected

urlpatterns = patterns('',
                       url(r'^$', index, name='games_index'),
                       url(r'^add/$', add, name='games_add'),
                       url(r'^show/(?P<id>\w+)/', show, name='game_show'),
                       url(r'^show_rejected/(?P<id>\w+)/',
                           show_rejected, name='game_show_rejected'),
                       url(r'^edit/(?P<id>\w+)/', edit, name='game_edit'),
                       url(r'^edit_approval/(?P<id>\w+)/',
                           edit_approval, name='game_edit_approval'),
                       url(r'^add/score/(?P<id>\w+)/',
                           add_score, name='game_add_score'),
                       url(r'^wins/', wins, name='page_wins'),
                       url(r'^losts/', losts, name='page_losts'),
                       url(r'^draws/', draws, name='page_draws'),
                       url(r'^for_approval/$', for_approval, name='approvals'),
                       url(r'^rejected/$', rejected, name='page_rejected')
                       )

import os,hashlib
import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection


class Game(models.Model):

    TENNIS = 1
    CHESS = 2

    CATEGORIES = (
        (TENNIS, 'tennis'),
        (CHESS, 'chess'),
    )

    NONE = 0,
    FIRST_WIN = 1
    FIRST_LOSE = 2
    DRAW = 3

    STATUSES = (
        (NONE,'none'),
        (DRAW, 'draw'),
        (FIRST_WIN, 'first_win'),
        (FIRST_LOSE, 'first_lose'),
    )

    title = models.CharField(max_length=255,blank=False, null=False)
    category = models.IntegerField(choices=CATEGORIES,default=0)
    status = models.IntegerField(choices=STATUSES,default=0)
    first_player =  models.ForeignKey(User,related_name='%(class)s_first')
    second_player =  models.ForeignKey(User,related_name='%(class)s_second')
    played_date = models.DateTimeField(default = datetime.datetime.now,blank=True)
    
    class Meta:
        db_table = 'games'

class GameScore(models.Model):
    
    game =  models.ForeignKey(Game)
    first_player =  models.ForeignKey(User,related_name='%(class)s_first')
    second_player =  models.ForeignKey(User,related_name='%(class)s_second')
    first_score = models.IntegerField()
    second_score = models.IntegerField()
    played_time = models.IntegerField(blank=True, null=True) # time in seconds 

    class Meta:
        db_table = 'scores'
    
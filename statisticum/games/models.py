import os
import hashlib
import datetime

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection


class GameManager(models.Manager):

    def wins(self, player):
        first_win = Q(first_player=player) & Q(status=Game.FIRST_WIN)
        second_lose = Q(second_player=player) & Q(status=Game.FIRST_LOSE)
        approved = Q(approver_status=Game.APPROVED)

        return Game.objects.filter((first_win | second_lose) & approved)

    def losts(self, player):
        first_lose = Q(first_player=player) & Q(status=Game.FIRST_LOSE)
        second_lose = Q(second_player=player) & Q(status=Game.FIRST_WIN)
        approved = Q(approver_status=Game.APPROVED)
        return Game.objects.filter((first_lose | second_lose) & approved)

    def draws(self, player):
        draw_first = Q(first_player=player) & Q(status=Game.DRAW)
        draw_second = Q(second_player=player) & Q(status=Game.DRAW)
        approved = Q(approver_status=Game.APPROVED)
        return Game.objects.filter((draw_first | draw_second) & approved)

    def games_to_approve(self, player):
        return Game.objects.filter(Q(approver_status=Game.NOT_APPROVED) &
                                   Q(approver=player))

    def rejected(self, player):
        return Game.objects.filter(Q(approver_status=Game.REJECTED) &
                                   Q(approver=player))


class Game(models.Model):

    TENNIS = 1
    CHESS = 2
    FOOTBALL = 3
    BASKETBALL = 4
    HOCKEY = 5

    CATEGORIES = (
        (TENNIS, 'tennis'),
        (CHESS, 'chess'),
        (FOOTBALL, 'football'),
        (BASKETBALL, 'basketball'),
        (HOCKEY, 'hockey'),
    )

    CATEGORIES_NAMES = dict((x, y) for x, y in CATEGORIES)

    NONE = 0
    FIRST_WIN = 1
    FIRST_LOSE = 2
    DRAW = 3

    STATUSES = (
        (NONE, 'none'),
        (DRAW, 'draw'),
        (FIRST_WIN, 'first_win'),
        (FIRST_LOSE, 'first_lose')
    )
    NOT_APPROVED = 0
    APPROVED = 1
    REJECTED = 2

    TO_APPROVE = (
        (REJECTED, 'rejected'),
        (APPROVED, 'approved')
    )

    title = models.CharField(max_length=255, blank=False, null=False)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    status = models.IntegerField(choices=STATUSES, default=0)
    first_player = models.ForeignKey(User, related_name='%(class)s_first')
    second_player = models.ForeignKey(User, related_name='%(class)s_second')
    played_date = models.DateTimeField(
        default=datetime.datetime.now, blank=True)
    approver = models.ForeignKey(User, related_name='%(class)s_approver')
    approver_status = models.IntegerField(choices=TO_APPROVE, default=0)
    comment = models.CharField(max_length=255, blank=True, null=True)

    objects = GameManager()

    def category_name(self):
        return Game.CATEGORIES_NAMES.get(self.category)

    class Meta:
        db_table = 'games'


class GameScore(models.Model):

    game = models.ForeignKey(Game)
    first_player = models.ForeignKey(User, related_name='%(class)s_first')
    second_player = models.ForeignKey(User, related_name='%(class)s_second')
    first_score = models.IntegerField()
    second_score = models.IntegerField()
    played_time = models.IntegerField(blank=True, null=True)  # time in seconds

    class Meta:
        db_table = 'scores'

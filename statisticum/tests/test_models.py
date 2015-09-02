import datetime
import hashlib
import re

from django.test import TestCase
from django.utils import six
from django.contrib.auth.models import User
from statisticum.games.models import Game, GameScore
from statisticum.profiles.models import UserProfile


class UserTests(TestCase):

    user_data = {'username': 'bo',
                 'password': 'creativ3',
                 'email': 'bo@gmail.com'}

    def test_user_creation(self):
        new_user = User(**self.user_data)
        new_user.save()

        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        profile = UserProfile.objects.get(user=new_user)
        self.assertEqual(None, profile.gender)
        profile.gender = UserProfile.GENDER_MALE
        profile.save()

        profile = UserProfile.objects.get(user=new_user)
        self.assertTrue(UserProfile.GENDER_MALE, profile.gender)


class GameTests(TestCase):

    fixtures = ['users.json', 'games.json']

    def setUp(self):
        self.first = User.objects.get(pk=1)
        self.second = User.objects.get(pk=2)

    def test_model(self):
        pass

    def test_wins(self):
        self.assertEqual(Game.objects.wins(self.first).count(), 3)
        self.assertEqual(Game.objects.wins(self.second).count(), 1)

    def test_losts(self):
        self.assertEqual(Game.objects.losts(self.first).count(), 1)
        self.assertEqual(Game.objects.losts(self.second).count(), 3)

    def test_draws(self):
        self.assertEqual(Game.objects.draws(self.first).count(), 3)
        self.assertEqual(Game.objects.draws(self.second).count(), 3)

    def test_category(self):
        game = Game()
        self.assertEqual(None, game.category_name())

        game.category = Game.TENNIS
        self.assertEqual('tennis', game.category_name())

        game.category = Game.CHESS
        self.assertEqual('chess', game.category_name())

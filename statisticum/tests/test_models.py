import datetime
import hashlib
import re

from django.test import TestCase

from statisticum.games.models import Game, GameScore
from statisticum.profiles.models import UserProfile
class UserModelTests(TestCase):

    user_info = {'username': 'Bozhidar',
                 'password': 'creativ3',
                 'email': 'bojidariv@gmail.com'}

    def teast_user_profile_creation(self):
        new_user = User(**self.user_info)
        new_user.save()

        self.assertEqual(UserProfile.objects.count(), 1)
        profile = UserProfile.objects.get(user=new_user)
        self.assertEqual(profile.user.id, new_user.id)
        self.assertEqual(six.text_type(profile),"Registration information for Bozhidar")

   

   

class GameModelTests(TestCase):

    def test_game_fields(self):
        game = Game()
    
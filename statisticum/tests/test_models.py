import datetime
import hashlib
import re

from django.utils import six
from django.conf import settings
from django.contrib.sites.models import Site
from django.core import mail
from django.core import management
from django.test import TestCase

from registration.models import RegistrationProfile
from registration.users import UserModel
from statisticum.games.models import Game, GameScore

class RegistrationModelTests(TestCase):
    """
    Test the model and manager used in the default backend.

    """
    user_info = {'username': 'Bozhidar',
                 'password': 'creativ3',
                 'email': 'bojidariv@gmail.com'}

    def test_profile_creation(self):
        """
        Creating a registration profile for a user populates the
        profile with the correct user and a SHA1 hash to use as
        activation key.

        """
        new_user = UserModel().objects.create_user(**self.user_info)
        profile = RegistrationProfile.objects.create_profile(new_user)

        self.assertEqual(RegistrationProfile.objects.count(), 1)
        self.assertEqual(profile.user.id, new_user.id)
        self.assertEqual(six.text_type(profile),
                         "Registration information for Bozhidar")

    def test_user_creation(self):
        """
        Creating a new user populates the correct data, and sets the
        user's account inactive.

        """
        new_user = RegistrationProfile.objects.create_inactive_user(site=Site.objects.get_current(),
                                                                        username='bob',
                                                                        password='secret',
                                                                        email='bob@example.com')
        self.assertEqual(new_user.username, 'bob')
        self.assertEqual(new_user.email, 'bob@example.com')
        

   

class GameModelTests(TestCase):
    
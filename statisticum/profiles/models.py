import os
import hashlib
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection
from django.db.models.signals import post_save


def set_user_password(user, password):
    if user and password:
        password = password.encode("utf-8")
        user.password = hashlib.md5(password).hexdigest()


User.set_password = set_user_password


class UserProfile(models.Model):

    GENDER_MALE = 1
    GERNDER_FEMALE = 2

    GENDERS = (
        (GENDER_MALE, 'male'),
        (GERNDER_FEMALE, 'famale')
    )

    DEFAULT_PROFILE_IMAGE = "profile/avatar.gif"

    user = models.ForeignKey(User)
    gender = models.IntegerField(choices=GENDERS, blank=True, null=True)

    class Meta:
        db_table = 'profiles'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

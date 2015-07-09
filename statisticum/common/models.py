import os,hashlib
import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection




def set_user_password(user,password):
    if user and password:
        password = password.encode("utf-8")
        user.password = hashlib.md5(password).hexdigest()

User.set_password = set_user_password

class UserProfile(models.Model):
    
    GENDERS = (
        (1,'male'), 
        (2,'famale')
    )
    
    DEFAULT_PROFILE_IMAGE = "profile/avatar.gif"
    
    user = models.ForeignKey(User)   
    gender = models.IntegerField(choices=GENDERS,blank=False )
  
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 'profiles'
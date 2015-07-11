import os,hashlib
import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection


class Profile(models.Model):

   
    GENDERS = (
        (1,'male'), 
        (2,'famale')
    )
    
    first_name = models.CharField(max_length=255,blank=False, null=False)
    last_name = models.CharField(max_length=255,blank=False, null=False)
    gender = models.IntegerField(choices=GENDERS,blank=False )
    residence = models.CharField(max_length=255,blank=False, null=False)
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 'profiles'
    
   

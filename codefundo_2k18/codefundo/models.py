from django.db import models
from django.contrib.auth.models import User
class user_details(models.Model):
    aadhar_no =models.IntegerField(default=0,unique=True)
    pincode   =models.IntegerField(default = 0)
    city  = models.TextField(max_length=15,default="asdf")

class track_users(models.Model):
    pincode = models.IntegerField( default=0,unique=True)
    user_count=models.IntegerField(default=0)
    city  = models.TextField(max_length=15,default="asdf")
    fund = models.IntegerField(default=0)

class gov_fund(models.Model):
    fund = models.IntegerField(default=0)

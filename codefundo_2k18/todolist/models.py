from django.db import models
from django.contrib.auth.models import User
class liste(models.Model):
    list_todo =models.TextField(default="enter text",unique=False)
    
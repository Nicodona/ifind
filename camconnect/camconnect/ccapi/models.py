import datetime

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    category = models.CharField(max_length=24)
    location = models.CharField(max_length=20)
    mention = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="pictures")
    desc = models. CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add = True)



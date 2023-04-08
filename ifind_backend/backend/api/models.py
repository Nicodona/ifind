from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token




class Register(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(upload_to='picture', null=True, blank=True)
    phone = PhoneNumberField(max_length=13, null=True, blank=True)
    profession = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.name




class Found(models.Model):
    image = models.ImageField(upload_to='img_found', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    isFound = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-updated']
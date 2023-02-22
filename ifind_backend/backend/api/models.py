from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

region_choices = [
    'NW', 'SW', 'STH','LIT', 'CT', 'ADM', 'FNTH', 'NTH', 'EST', 'WST',
]


class Register(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=10, choices=region_choices,null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(upload_to='picture', null=True, blank=True)
    phone = PhoneNumberField()
    profession = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.name[::]
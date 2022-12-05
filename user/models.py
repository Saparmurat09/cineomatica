from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)

    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=100, blank=False)

    is_admin = models.BooleanField(default=False)

    birth_date = models.DateField(blank=True, null=True)




class ClubCard(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    spent = models.FloatField(default=0)
    discount = models.FloatField(default=0)

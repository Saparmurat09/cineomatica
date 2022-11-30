from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)

    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=100, blank=False)

    is_admin = models.BooleanField(default=False)

    birth_date = models.DateField()

    # TODO add clubcard creation


class ClubCard(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    spent = models.FloatField(default=0)
    discount = models.FloatField(default=0)

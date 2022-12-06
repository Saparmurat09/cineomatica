from django.db import models
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from user.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    poster = models.URLField(blank=True)

    duration = models.DurationField()

    year = models.DateField()

    director = models.CharField(max_length=100)

    GENRES = [
        (1, _("Horror")),
        (2, _("Thriller")),
        (3, _("Comedy")),
        (4, _("Western")),
        (5, _("Sci-Fi")),
        (6, _("Fantasy")),
    ]

    genre = models.IntegerField(choices=GENRES, blank=True)

    language = models.CharField(max_length=100, blank=False)
    
    country = CountryField()


    class Status(models.TextChoices):
        ACTIVE = 1, _('active')
        UPCOMING = 2, _('upcoming')
        INACTIVE = 3, _('inactive')

    status = models.IntegerField(choices=Status.choices, blank=False, default=Status.ACTIVE)

    class Rating(models.IntegerChoices):
        AGE_21 = 1, _("21+")
        AGE_18 = 2, _("18+")
        AGE_16 = 3, _("16+")
        AGE_12 = 4, _("12+")
        AGE_6 = 5, _("6+")
    

    age_rating = models.IntegerField(choices=Rating.choices, blank=False, default=Rating.AGE_6)


class Cinema(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)


class Address(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    city = models.CharField(max_length=100, blank=False)
    district = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=False)
    number = models.CharField(max_length=100, blank=False)


class Contact(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    mail = models.EmailField(max_length=256)
    number = models.CharField(max_length=100, blank=False)


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    row = models.IntegerField()
    collumn = models.IntegerField()


class Feedback(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.CharField(max_length=1000, blank=False)
    
    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    rating = models.IntegerField(choices=RATING, blank=False)

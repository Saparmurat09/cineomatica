from django.db import models
from languages.fields import LanguageField
from django_countries.fields import CountryField


class Movie(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    poster = models.URLField(blank=True)

    duration = models.DurationField()

    year = models.DateField()

    director = models.CharField(max_length=100)

    GENRES = (
        (1, "Horror"),
        (2, "Thriller"),
        (3, "Comedy"),
        (4, "Western"),
        (5, "Sci-Fi"),
        (6, "Fantasy"),
    )

    genre = models.Choices(GENRES)
    language = LanguageField()
    country = CountryField()


    STATUS = (
        (1, 'active'),
        (2, 'upcoming'),
        (3, 'inactive'),
    )

    status = models.Choices(STATUS)

    RATING = (
        (1, "21+"),
        (2, "18+"),
        (3, "16+"),
        (4, "12+"),
        (5, "6+"),
    )

    age_rating = models.Choices(RATING)


class Cinema(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)


class Address(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    
    city = models.CharField(max_length=100, blank=False)
    district = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=False)
    number = models.CharField(max_length=100, blank=False)


class Contacts(models.Model):
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

    # TODO add user as foreign key

    content = models.CharField(max_length=1000, blank=False)
    
    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    rating = models.IntegerChoices(RATING)

from django.db import models
from cinema.models import Movie, Room, Seat, Session
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    time = models.TimeField(auto_now=True)

    total_price = models.FloatField(default=0)

    paid = models.BooleanField(default=False)

    payment_method = models.CharField(max_length=16, help_text='Enter Credit Card', null=True)


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)

    CATEGORY = (
        (1, "Children"),
        (2, "Student"),
        (3, "Adult"),
    )

    category = models.IntegerField(choices=CATEGORY, blank=False)


class BookTicket(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()

    CATEGORY = (
        (1, "Children"),
        (2, "Student"),
        (3, "Adult"),
    )

    category = models.IntegerField(choices=CATEGORY, blank=False)
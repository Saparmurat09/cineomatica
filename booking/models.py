from django.db import models
from cinema.models import Movie, Room, Seat, Session
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    time = models.TimeField(auto_created=True)

    total_price = models.FloatField(default=0)


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
    count = models.IntegerField(default=1)

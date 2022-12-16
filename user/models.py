from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required field')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('superuser must have is_staff = True') 

        if not extra_fields.get('is_superuser'):
            raise ValueError('superuser must have is_superuser = True') 

        user = self.create_user(email, password, **extra_fields)        

        return user


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)

    email = models.EmailField(max_length=256, blank=False, unique=True)
    phone = models.CharField(max_length=100, blank=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {self.name} {self.surname} - {self.id}"


class ClubCard(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    spent = models.FloatField(default=0)
    discount = models.FloatField(default=0)

    def __str__(self):
        return self.user.name
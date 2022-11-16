from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import birth_date_validator


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=8, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, "Пользователь"),
        (ADMIN, "Администратор"),
        (MODERATOR, "Модератор"),
    )


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=20)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(validators=[birth_date_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

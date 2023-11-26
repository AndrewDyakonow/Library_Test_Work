from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Users(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    date_registration = models.DateField(auto_now_add=now, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}, {self.email}'

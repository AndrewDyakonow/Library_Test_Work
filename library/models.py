from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import now


class Book(models.Model):
    """Модель книги"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=63, verbose_name='Название')
    author = models.CharField(max_length=63, verbose_name='Автор')
    year = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(now().year)
        ],
        verbose_name='Год издания'
    )
    isbn = models.CharField(max_length=20, verbose_name='Международный стандартный книжный номер')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, {self.author}, {self.year}, {self.isbn}'

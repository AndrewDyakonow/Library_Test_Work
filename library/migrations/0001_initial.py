# Generated by Django 4.2.7 on 2023-11-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=63, verbose_name='Название')),
                ('author', models.CharField(max_length=63, verbose_name='Автор')),
                ('year', models.DateField(verbose_name='Год издания')),
                ('isbn', models.CharField(max_length=20, verbose_name='Международный стандартный книжный номер')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
    ]


<h1 align="center">Test Work Library</h1>

<h2 align="center"> Тестовое задание </h2>

<div align="center">
    
<div>
    <a href="https://www.django-rest-framework.org/"><img alt="Static Badge" src="https://img.shields.io/badge/DRF-3.14.0-blue?labelColor=gray"></a>
    <a href="https://pypi.org/project/pymysql/"><img alt="Static Badge" src="https://img.shields.io/badge/pymysql-1.1.0-green?labelColor=gray"></a>
    <a href="https://cryptography.io/en/latest/"><img alt="Static Badge" src="https://img.shields.io/badge/cryptography-41.1.5-red?labelColor=gray"></a>
    <a href="https://docs.celeryq.dev/en/stable/"><img alt="Static Badge" src="https://img.shields.io/badge/celery-5.3.6-darkblue?labelColor=gray"></a>
    <a href="https://docs.pydantic.dev/latest/concepts/pydantic_settings/"><img alt="Static Badge" src="https://img.shields.io/badge/pydantic settings-2.1.0-darkviolet?labelColor=gray"></a>
    <a href="https://pypi.org/project/async-timeout/"><img alt="Static Badge" src="https://img.shields.io/badge/async_timeout-2.1.0-darkgreen?labelColor=gray"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.djangoproject.com/"><img width="48" height="48" src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="python"/></a>
    <a href="https://redis.io/"><img width="48" height="48" src="https://img.icons8.com/color/48/redis.png" alt="redis"/></a>
    <a href="https://www.docker.com/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker"/></a>
</div>

</div>

___

<h2>1. Установка</h2>

1.1 Клонируйте проект:
    
```bash
    git clone git@github.com:AndrewDyakonow/Library_Test_Work.git
```

1.2 Выполните команду построения докер образа и запуска контейнеров
```bash
    docker-compose up --build
```

1.3 Дождитесь появления в терминале события:
```
    web_app | Watching for file changes with StatReloader
```

___

<h2>2. Работа</h2>

2.1 Приложение доступно по адресу http://127.0.0.1:8001/.

<h3>2.2 Эндпоинты </h3>
<h4>2.2.1 library</h4>
* POST ``http://127.0.0.1:8001/book/create/`` -создать книгу.

В тело запроса передаются следующие параметры:

```
{
    "isbn": str,
    "title": str,
    "author": str,
    "year": int
}
```

* GET ``http://127.0.0.1:8001/book/list/`` -Смотреть список книг.
* GET ``http://127.0.0.1:8001/book/detail/X/`` - где X - id книги. Смотреть конкретную книгу.  
* PATCH ``http://127.0.0.1:8001/book/update/X/`` -где X - id книги. Редактировать запись.

В тело запроса передаются параметры, которые необходимо изменить:

```
{
    "title": "The Old Man and the Sea",
    "author": "Ernest Miller Hemingway",
}
```

* DELETE ``http://127.0.0.1:8001/book/delete/X/`` -где X - id книги. Удалить запись.


<h4>2.2.2 Users </h4>
* POST ``http://127.0.0.1:8001/users/registration/`` -Зарегистрироваться.

В тело запроса передаются следующие параметры:

```
{
    "email": str,
    "username": str,
    "password": str
}
```

<h2>3. Комментарий</h2>
Для удобства рекомендуется выполнять запросы с помощью API-платформы для разработчиков POSTMAN.
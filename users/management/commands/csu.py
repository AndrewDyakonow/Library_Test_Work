from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):
    """bash команда для создания супер-юзера"""

    def handle(self, *args, **options):
        user = Users.objects.create(
            email='andrewdyakonov@yahoo.com',
            first_name='Admin',
            last_name='Library',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe456rty')
        user.save()

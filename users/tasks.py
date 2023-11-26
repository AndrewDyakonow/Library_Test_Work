from celery import shared_task
from django.core.mail import send_mail

from env_setting import smtp_setting


@shared_task
def send_mail_new_user(user_email):
    send_mail(
        "Здравствуйте!",
        f"""Вы зарегистрировались!""",
        smtp_setting.EMAIL_HOST_USER,
        recipient_list=[user_email],
    )

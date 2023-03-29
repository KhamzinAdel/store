from django.core.mail import send_mail

from store.celery import app

from .models import Mailing
from .services import (email_contact, email_send_mailing,
                       logic_send_email_verification)


@app.task
def send_email_contact(**kwargs):
    email_contact(**kwargs)


@app.task
def send_spam_email(user_email: str):
    email_send_mailing(user_email)


@app.task
def send_beat_email():
    for contact_email in Mailing.objects.values('email'):
        send_mail(
            'Вы подписаны на рассылку',
            'Мы будем присылать уведомления о новых скидках',
            'hamzinadel@yandex.ru',
            [contact_email['email']],
            fail_silently=False,
        )


@app.task
def send_email_verification(user_id: int):
    logic_send_email_verification(user_id)

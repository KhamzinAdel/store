from django.core.mail import send_mail
from store.celery import app

from .services import email_send_mailing, email_contact, logic_send_email_verification
from .models import Mailing


@app.task
def send_email_contact(**kwargs):
    email_contact(**kwargs)


@app.task
def send_spam_email(user_email: str):
    email_send_mailing(user_email)


@app.task
def send_beat_email():
    for contact_email in Mailing.objects.all():
        send_mail(
            'Вы подписаны на рассылку',
            'Мы будем присылать вам письмо каждые 5 минут.',
            'hamzinadel@yandex.ru',
            [contact_email.email],
            fail_silently=False,
        )


@app.task
def send_email_verification(user_id: str):
    logic_send_email_verification(user_id)


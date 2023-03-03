import uuid
from datetime import timedelta

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.timezone import now

from users.models import User, EmailVerification


def email_contact(**kwargs):
    subject = 'Обратная связь'
    html_message = render_to_string('users/contact_email.html', {
        'name': kwargs.get('name'),
        'email': kwargs.get('email'),
        'content': kwargs.get('content'),
    })
    send_mail(subject,
              html_message,
              'hamzinadel@yandex.ru',
              ['khamzin.adel@mail.ru'],
              )


def email_send_mailing(user_email: str):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем уведомлять вас о новых скидках',
        'hamzinadel@yandex.ru',
        [user_email],
        fail_silently=False,
    )


def logic_send_email_verification(user_id: str):
    user = User.objects.get(pk=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()

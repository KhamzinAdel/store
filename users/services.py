from django.core.mail import send_mail
from django.template.loader import render_to_string


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

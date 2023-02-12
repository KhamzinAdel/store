from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_verified_email = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = 'Для подтверждения учетной записи для {} перейдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        html_message = 'Для подтверждения учетной записи для {} перейдите по <a href="{}">ссылке</a>'.format(
            self.user.email,
            verification_link
        )

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
            html_message=html_message
        )

    def is_expired(self):
        return True if now() >= self.expiration else False


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    content = models.TextField()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class StarRating(models.Model):
    value = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

    def __str__(self):
        return f'{self.value}'


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    star_rating = models.ForeignKey('StarRating', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def get_absolute_url(self):
        return reverse('users:review_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} - {self.star_rating}'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from common.views import TitleMixin
from .services import email

from .forms import (ContactForm, UserLoginForm, UserProfileForm,
                    UserRegistrationForm, ReviewsForm)
from .models import Contact, EmailVerification, User, Reviews, StarRating


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'

    def get_success_url(self):
        return reverse_lazy('index')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы'
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class ContactFormView(TitleMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    title = 'Обратная связь'
    template_name = 'users/contact.html'
    success_url = reverse_lazy('users:contact')
    success_message = 'Сообщение отправлено'

    def form_valid(self, form):
        data = form.data
        email(name=data['first_name'], email=data['email'], content=data['content'])
        return super().form_valid(form)


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return redirect('index')


class ReviewView(TitleMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'users/reviews.html'
    success_url = reverse_lazy('users:reviews')
    success_message = 'Отзыв отправлен'
    title = 'Отзывы'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        star_rating = self.kwargs.get('star_rating')
        context['count_review'] = Reviews.objects.count()
        context['stars_rating'] = StarRating.objects.all()
        context['reviews'] = Reviews.objects.filter(star_rating=star_rating) if star_rating else Reviews.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Reviews
    context_object_name = 'review'
    template_name = 'users/review_delete.html'
    success_url = reverse_lazy('users:reviews')


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Reviews
    template_name = 'users/review_update.html'
    success_url = reverse_lazy('users:reviews')
    fields = ('star_rating', 'text')

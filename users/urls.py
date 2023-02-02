from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('reviews/', views.ReviewView.as_view(), name='reviews'),
    path('reviews/delete/<int:review_id>', views.ReviewViewDelete.as_view(), name='review_delete'),
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='email_verification'),
]

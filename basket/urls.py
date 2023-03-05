from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
]

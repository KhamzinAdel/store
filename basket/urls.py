from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', views.BasketAdd.as_view(), name='basket_add'),
    path('remove/<int:product_id>/', views.BasketRemove.as_view(), name='basket_remove'),
]

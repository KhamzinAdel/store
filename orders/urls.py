from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order-create/', views.OrderCreateView.as_view(), name='order_create'),
    path('', views.OrderListView.as_view(), name='orders_list'),
    path('order-success/', views.SuccessTemplateView.as_view(), name='order-success'),
    path('order-canceled/', views.CanceledTemplateView.as_view(), name='order-canceled'),
]

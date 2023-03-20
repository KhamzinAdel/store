from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', views.BasketAddView.as_view(), name='basket_add'),
    path('remove/<int:product_id>/', views.BasketRemoveView.as_view(), name='basket_remove'),
    path('coupon/', views.CouponView.as_view(), name='coupon'),
]

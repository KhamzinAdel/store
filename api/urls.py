from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views_orders, views_products, views_users

app_name = 'api'

router = DefaultRouter()
router.register(r'review', views_users.ReviewViewSet)
router.register(r'product', views_products.ProductViewSet, basename='queryset')

urlpatterns = [
    path('product_category/', views_products.ProductCategoryListAPIView.as_view(), name='product_category'),
    path('contact/', views_users.ContactCreateAPIView.as_view(), name='contact'),
    path('mailing/', views_users.MailingCreateAPIView.as_view(), name='mailing'),
    path('order/', views_orders.OrderListCreateAPIView.as_view(), name='order'),
]

urlpatterns += router.urls

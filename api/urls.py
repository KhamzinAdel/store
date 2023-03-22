from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views_products, views_users

app_name = 'api'

router = DefaultRouter()
router.register(r'review', views_users.ReviewViewSet)

urlpatterns = [
    path('product_list/', views_products.ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>', views_products.ProductDetailAPIView.as_view(), name='product_detail'),
    path('product_category/', views_products.ProductCategoryListAPIView.as_view(), name='product_category'),
    path('contact/', views_users.ContactCreateAPIView.as_view(), name='contact'),
    path('mailing/', views_users.MailingCreateAPIView.as_view(), name='mailing'),
]

urlpatterns += router.urls

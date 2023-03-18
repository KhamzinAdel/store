from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('product_list/', views.ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>', views.ProductDetailAPIView.as_view(), name='product_detail'),
    path('product_category/', views.ProductCategoryListAPIView.as_view(), name='product_category')
]

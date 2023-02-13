from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>', views.ProductsListView.as_view(), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]


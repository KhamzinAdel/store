from django.urls import include, path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>', views.ProductsListView.as_view(), name='category'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('favorites/', include('favorites.urls', namespace='favorites')),
]

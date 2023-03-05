from django.urls import include, path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'products'

urlpatterns = [
    path('', cache_page(60)(views.ProductsListView.as_view()), name='products'),
    path('category/<int:category_id>', cache_page(60)(views.ProductsListView.as_view()), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('favorites/', include('favorites.urls', namespace='favorites')),
]

from django.urls import path

from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorites_list, name='favorites_list'),
    path('add/<int:product_id>/', views.add_to_favorites, name='favorites_add'),
    path('remove/<int:product_id>/', views.remove_from_favorites, name='favorites_remove'),
    path('delete/', views.delete_favorites, name='favorites_delete'),
]

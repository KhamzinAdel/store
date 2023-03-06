from django.urls import path

from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.FavoriteListView.as_view(), name='favorites_list'),
    path('add/<int:product_id>/', views.AddToFavoriteView.as_view(), name='favorites_add'),
    path('remove/<int:product_id>/', views.RemoveFromFavoriteView.as_view(), name='favorites_remove'),
    path('delete/', views.DeleteFavoriteView.as_view(), name='favorites_delete'),
]

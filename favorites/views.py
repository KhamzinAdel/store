from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Product

from .favorite import Favorites


class FavoriteListView(TitleMixin, LoginRequiredMixin, ListView):
    title = 'Избранное'
    template_name = 'favorites/favorites-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        favorite = Favorites(self.request)
        return Product.objects.filter(pk__in=favorite.favorite_list())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite = Favorites(self.request)
        context['len_products'] = len(favorite.favorite_list())
        return context


class AddToFavoriteView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        favorite = Favorites(request)
        favorite.add(product_id=self.kwargs.get('product_id'))
        return redirect(request.META['HTTP_REFERER'])


class RemoveFromFavoriteView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        favorites = Favorites(request)
        favorites.remove(product_id=self.kwargs.get('product_id'))
        return redirect(request.META['HTTP_REFERER'])


class DeleteFavoriteView(LoginRequiredMixin, View):

    @staticmethod
    def post(request, *args, **kwargs):
        favorites = Favorites(request)
        favorites.delete()
        return redirect(request.META['HTTP_REFERER'])

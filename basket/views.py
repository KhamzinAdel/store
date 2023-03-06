from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product
from .basket import Basket


class BasketAdd(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        basket.add(product=product)
        return redirect(request.META['HTTP_REFERER'])


class BasketRemove(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        basket.remove(product)
        return redirect(request.META['HTTP_REFERER'])

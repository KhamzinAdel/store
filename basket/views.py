from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from products.models import Product
from .basket import Basket


@login_required
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.add(product=product)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect(request.META['HTTP_REFERER'])

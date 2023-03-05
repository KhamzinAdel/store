from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.models import Product
from .favorites import Favorites


@login_required
def favorites_list(request):
    favorites = request.session.get('favorites', [])
    products = Product.objects.filter(pk__in=favorites)
    len_products = len(favorites)
    context = {
        'title': 'Избранное',
        'products': products,
        'len_products': len_products,
    }
    return render(request, 'favorites/favorites-list.html', context=context)


@login_required
def add_to_favorites(request, product_id):
    favorites = Favorites(request)
    favorites.add(product_id=product_id)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_favorites(request, product_id):
    favorites = Favorites(request)
    favorites.remove(product_id=product_id)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def delete_favorites(request):
    favorites = Favorites(request)
    favorites.delete()
    return redirect(request.META['HTTP_REFERER'])

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from products.models import Product


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
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])
    request.session['favorites'].append(product_id)
    return redirect(request.META['HTTP_REFERER'])


def remove_from_favorites(request, product_id):
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item == product_id:
                request.session['favorites'].remove(item)

        while [] in request.session['favorites']:
            request.session['favorites'].remove([])

        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True
        return redirect(request.META['HTTP_REFERER'])


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']
    return redirect(request.META['HTTP_REFERER'])

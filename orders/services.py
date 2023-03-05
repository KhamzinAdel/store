import stripe
import geocoder

from django.conf import settings
from django.urls import reverse

from basket.basket import Basket


def geo_address(address: str) -> list:
    geo = geocoder.mapbox(address, key=settings.MAPBOX_PUBLIC_TOKEN)
    geo = geo.latlng  # [lat, long]
    return geo


def stripe_api(request, object_id):
    baskets = Basket(request)
    checkout_session = stripe.checkout.Session.create(
        line_items=baskets.stripe_products(),
        metadata={'order_id': object_id},
        mode='payment',
        success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order-success')),
        cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order-canceled')),
    )
    return checkout_session



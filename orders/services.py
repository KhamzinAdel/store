import geocoder

from django.conf import settings


def geo_address(address: str) -> list:
    geo = geocoder.mapbox(address, key=settings.MAPBOX_PUBLIC_TOKEN)
    geo = geo.latlng  # [lat, long]
    return geo



from django.core.cache import cache
from django.db.models.query import QuerySet


def cashes_product(cashes_get: str, queryset: QuerySet, time: int) -> QuerySet:
    product = cache.get(cashes_get)
    if not product:
        product = queryset
        cache.set(cashes_get, product, time)

    return product

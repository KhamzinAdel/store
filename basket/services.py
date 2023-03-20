from django.utils import timezone
from django.http import HttpRequest

from .models import Coupon


def coupon_get(request: HttpRequest, code: str):
    now = timezone.now()
    try:
        coupon = Coupon.objects.get(code__iexact=code,
                                    valid_from__lte=now,
                                    valid_to__gte=now,
                                    active=True)
        request.session['coupon_id'] = coupon.id
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None

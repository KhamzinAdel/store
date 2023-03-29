from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import FormView

from products.models import Product

from .basket import Basket
from .forms import CouponForm
from .services import coupon_get


class BasketAddView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        basket.add(product)
        return redirect(request.META['HTTP_REFERER'])


class BasketRemoveView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        basket.remove(product)
        return redirect(request.META['HTTP_REFERER'])


class CouponView(FormView):
    template_name = 'basket/coupon.html'
    form_class = CouponForm

    def get_success_url(self):
        return redirect(self.request.META['HTTP_REFERER'])

    def form_valid(self, form):
        code = form.cleaned_data.get('code')
        coupon_get(self.request, code)
        return super().form_valid(form)

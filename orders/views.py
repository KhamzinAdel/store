import stripe
from http import HTTPStatus

from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.conf import settings

from common.views import TitleMixin
from .forms import OrderForm
from products.models import Basket
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    title = 'Store - Спасибо за заказ!'
    template_name = 'orders/success.html'


class CanceledTemplateView(TemplateView):
    template_name = 'orders/canceled.html'


class OrderListView(TitleMixin, ListView):
    title = 'Store - Заказы'
    template_name = 'orders/orders.html'
    context_object_name = 'orders'
    ordering = ('-created',)

    def get_queryset(self):
        return Order.objects.all() if self.request.user.is_superuser else Order.objects.filter(initiator=self.request.user)


class OrderCreateView(TitleMixin, CreateView):
    title = 'Store - Оформление заказа'
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(),
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order-success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order-canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

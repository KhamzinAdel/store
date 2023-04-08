import stripe
from http import HTTPStatus

from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from orders.models import Order

from .forms import OrderForm
from .services import stripe_api

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
        return Order.objects.filter(initiator=self.request.user).select_related('initiator')


class OrderCreateView(TitleMixin, CreateView):
    title = 'Store - Оформление заказа'
    template_name = 'orders/order-create.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        checkout_session = stripe_api(request, self.object.id)
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

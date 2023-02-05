from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from common.views import TitleMixin
from .forms import OrderForm


class OrderCreateView(TitleMixin, CreateView):
    title = 'Store - Оформление заказа'
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderCreateSerializers, OrderListSerializers


class OrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(initiator=self.request.user)


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(initiator=self.request.user)
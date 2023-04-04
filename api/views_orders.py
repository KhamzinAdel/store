from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderCreateSerializer, OrderListSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(initiator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(initiator=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderListSerializer
        elif self.request.method == 'POST':
            return OrderCreateSerializer

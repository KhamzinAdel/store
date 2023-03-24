from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializers


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(initiator=self.request.user)

from rest_framework import serializers

from orders.models import Order


class OrderSerializers(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order
        fields = ('id', 'email', 'created', 'status')

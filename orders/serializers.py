from rest_framework import serializers

from orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order
        fields = ('id', 'email', 'created', 'status')


class OrderCreateSerializer(serializers.ModelSerializer):
    initiator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'initiator')

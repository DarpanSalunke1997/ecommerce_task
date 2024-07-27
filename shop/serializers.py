from rest_framework import serializers
from .models import Product, SeasonalProduct, BulkProduct, Discount, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price']

class SeasonalProductSerializer(ProductSerializer):
    class Meta:
        model = SeasonalProduct
        fields = ProductSerializer.Meta.fields + ['season_discount']

class BulkProductSerializer(ProductSerializer):
    class Meta:
        model = BulkProduct
        fields = ProductSerializer.Meta.fields + ['bulk_quantity', 'bulk_discount']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'discount_type', 'value']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'discount']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.items.all().delete()
        for item_data in items_data:
            OrderItem.objects.create(order=instance, **item_data)
        return super().update(instance, validated_data)

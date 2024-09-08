from rest_framework import serializers
from .models import Product,Stock,StockProduct
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    title = serializers.CharField(max_length=60)
    class Meta:
        model = Product
        fields = ['id','title','description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['id','product','quantity','price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for pos in positions:
            StockProduct.objects.create(stock=stock,**pos)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        StockProduct.objects.filter(stock=stock).delete()
        for pos in positions:
            StockProduct.objects.update_or_create(stock=stock,**pos)
        return stock
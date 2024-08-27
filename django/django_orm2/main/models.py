from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)

#Создаем таблицу от многих к многим, потом ее убираем.
#class Order(models.Model):
#    products = models.ManyToManyField(Product, related_name='orders')
class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders', through='OrderPosition')

class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()

#Получить доступ к продуктам из заказа можно
# order_products = some_order.products.all()
#Получить заказы в которых участвует продукт можно
# product_orders = some_product.orders.all()

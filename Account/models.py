import Product
from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class Cart(models.Model):
    User = models.ForeignKey(User, related_name="UserCart", on_delete=models.CASCADE)
    IsPaid = models.BooleanField()
    DateOfPay = models.DateTimeField(blank=True,null=True)

    def get_orders_cart(self):
        return Order.objects.filter(CartOrder = self.User)

    def get_order_price(self):
        price = 0
        orders = Order.objects.filter(CartOrder = self.User)
        for order in orders:
            price += order.get_products_price()
        return price


class Order(models.Model):
    CartOrder = models.ForeignKey(Cart, related_name="CartOrder", on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, related_name="ProductOrder", on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Count = models.IntegerField()


    def get_products_price(self):
        return self.Price * self.Count


    def __str__(self):
        return f'{self.Product.Name}'


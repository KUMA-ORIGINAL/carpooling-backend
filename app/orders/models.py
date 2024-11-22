from django.db import models

from accounts.models import User
from products.models import Product


class Order(models.Model):
    ORDER_STATUS = (
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('delivering', 'Delivering'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='orders', limit_choices_to={'role': 'client'})
    courier = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                related_name='deliveries', limit_choices_to={'role': 'courier'})
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order #{self.id} by {self.customer.username}'

    def calculate_total_price(self):
        self.total_price = sum(item.price * item.quantity for item in self.items.all())
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} in order {self.order.id}'
from django.db import models
from django.conf import settings
from products.models import Mobile


class Order(models.Model):
    '''
    This class creates user profile fields
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    description = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    '''
    This class specifies the user and the product he selected and its number
    '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Mobile', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

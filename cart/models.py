from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from products.models import Product

# My models here.

class Cart(models.Model):
    User            = models.ForeignKey(User,on_delete=models.CASCADE)
    creation_date   = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.User.username

class CartItem(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    price       = models.FloatField(blank=True)
    cart        = models.ForeignKey('Cart', on_delete=models.CASCADE)
    TAX_AMOUNT = 19.25

    def dtotal(self):
        return (self.price - self.product.discount ) * self.quantity

    def sprice(self):
        return self.price

    def discount(self):
        return self.product.discount

    def qnt(self):
        return self.quantity

    def __str__(self):
        return  self.product.name
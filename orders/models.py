from django.db import models
from datetime import datetime
from products.models import Product 
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    User = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ManyToManyField(Product,blank=True)
    buying_date = models.DateTimeField(auto_now_add=True)
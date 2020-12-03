from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import render,redirect ,reverse


# My models here.

class Product(models.Model):
    name      = models.CharField(max_length=100 ,blank=True)
    owner     = models.ForeignKey(User,on_delete=models.CASCADE)      
    slug      = models.SlugField(max_length = 250, null = True, blank = True) 
    detail    = models.CharField(max_length=300 ,blank=True)      
    price     = models.IntegerField(blank =True , null=True)
    discount  = models.IntegerField(blank =True , null=True)
    image     = models.FileField(upload_to='Products',blank=True)    
    quantity  = models.IntegerField(blank =True , null=True , default=0)          
    category  = models.CharField(max_length=100 ,blank=True)                
    total     = models.IntegerField(null=True,blank=True)
    
    def add_to_cart(self):
        return reverse("add-to-cart" , kwargs={
            'slug':self.slug
            })

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
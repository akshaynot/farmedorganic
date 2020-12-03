from django.forms import ModelForm
from products.models import Product
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name' ,'owner' ,'detail' ,'discount' ,'image','quantity' ,'category']
        

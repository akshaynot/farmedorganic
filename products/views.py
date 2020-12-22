from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView , CreateView , UpdateView , DeleteView , FormView
from django.db.models import Q # new
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm

@login_required
def CreateProduct(request):
    Pform = ProductForm 
    form = Pform(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        Pform = form
        name = Pform.cleaned_data['name']
        owner = request.user
        detail = Pform.cleaned_data['detail']
        price = Pform.cleaned_data['price']
        discount = Pform.cleaned_data['discount']
        image = Pform.cleaned_data['image']
        quantity = Pform.cleaned_data['quantity']    
        category = Pform.cleaned_data['category']
        
        # Creating product for validation
        NewProduct = Product(name=name,owner=owner,detail=detail,
        price=price,discount=discount,image=image,quantity=quantity,category=category)

        # Query to see if product already exists 
        Product_query = Product.objects.filter(name=NewProduct.name)
        if Product_query.exists():
            print("Product already exists")
        else:
            NewProduct = Product.objects.create(name=name,owner=owner,detail=detail,
            price=price,discount=discount,image=image,quantity=quantity,category=category)
            print(NewProduct.name , "added to the database" )

    else:
        pass
    context = {
        'form' : Pform 
    }
    return render(request,"CreateProduct.html",context)

class ProductDetailView(ListView):
    model = Product
    template_name = "ProductDetail.html"

class UpdateProductView(UpdateView):
    model = Product
    template_name = "UpdateProduct.html"
    
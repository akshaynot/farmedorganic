from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart , CartItem



@login_required
def cart(request):
    this_user = Cart.objects.get(User=request.user)
    this_Cart = CartItem.objects.filter(cart=this_user)

    if this_Cart.exists():
        items = CartItem.objects.all()
    else:
        print("Cart don't exist")
        items = None
    
    context = {
        'items':items,
    }
    return render(request,"cart.html",context)

@login_required
def add_to_cart(request,slug):
    this_user = Cart.objects.get(User=request.user)
    this_product = Product.objects.get(slug=slug)
    this_Cart = CartItem.objects.filter(cart=this_user)

    if(this_Cart.exists()):
        if(CartItem.objects.filter(product=this_product).exists()):
            pass
        else:
            newCart = CartItem(product=this_product ,price=3000,cart=this_user)    
            newCart.save()                
    else:
        newCart = CartItem(product=this_product ,price=3000,cart=this_user)    
        newCart.save()

    # this_product[0].save()
    # obj = Cart.objects.all().filter(User=this_user).get().products.all()
    print(CartItem.objects.all())        
    return redirect("cart")


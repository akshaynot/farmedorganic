from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.urls import reverse
from allauth.account.signals import user_logged_in , user_signed_up
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from .models import Cart , CartItem
from products.models import Product

cart_count = 0

@login_required
def cart(request):
    this_user = Cart.objects.get(User=request.user)
    this_Cart = CartItem.objects.filter(cart=this_user)
    subtotal = 0
    total = 0
    tax =0

    if this_Cart.exists():
        items = CartItem.objects.all()

        for i in items:
            subtotal += i.dtotal()
        total = subtotal-tax
        if total==0:
            tax =0
        else:
            tax =20
            total = subtotal-tax

    else:
        print("Cart don't exist")
        items = None
    
    if request.method == 'GET':
        name = request.GET.get('name', None)
        value = request.GET.get('value', None)
        # Updating cart
        if(this_Cart.exists()):
            if name:
                this_product = Product.objects.get(name=name)
                if(CartItem.objects.filter(product=this_product).exists()):
                    currentItem = CartItem.objects.get(product=this_product)
                    currentItem.quantity = value
                    total = currentItem.dtotal()
                    currentItem.save()
                    print(currentItem.price)
                else:
                    print(" CartItem don't exist.")
            else:
                print("Such product don't exist")
        else:
            print(" Cart don't exist.")
   
    cart_count =  CartItem.objects.all().count

    context = {
        'items':items,
        'cart_count':cart_count,
        'subtotal':subtotal,
        'tax':tax,
        'total':total,
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
            newCart = CartItem.objects.create(product=this_product ,price=3000,cart=this_user)    
    else:
        newCart = CartItem(product=this_product ,price=3000,cart=this_user)    
        newCart.save()

    return redirect("cart")

# removing itmes from cart
@login_required
def remove_from_cart(request,id):
    this_user = Cart.objects.get(User=request.user)
    this_product = CartItem.objects.get(id=id)
    this_Cart = CartItem.objects.filter(cart=this_user)

    if(this_Cart.exists()): # Checking if cart for logged in user exists 
        if(CartItem.objects.filter(id=id).exists()): # checking if certain product exits in cart
            this_product.delete()
        else:
            pass
    else:
        pass
    return redirect("cart")


# Creating cart on sign up
@receiver(user_signed_up)
def generateCart(sender, request, user, **kwargs):
    this_user = Cart.objects.filter(User=user)
    
    if not this_user.exists():
        NewCart = Cart.objects.create(User=user)

    else:
        pass
        print("Cart already exist")
    
    return reverse('profile')
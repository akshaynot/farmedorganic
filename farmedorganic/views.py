from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView , CreateView , UpdateView , DeleteView , FormView
from django.db.models import Q # new
from products.models import Product
from django.contrib.auth.models import User
from .forms import ProductForm
from cart.models import CartItem , Cart
from django.http import JsonResponse

# Create your views here.
def home(request):
    products = Product.objects.all()
    car_count = CartItem.objects.all().count()
    context = {
        'products':products,
        'cart_count':car_count,
    }
    return render(request,"home.html",context)

@login_required
def profile(request):
    user = request.user
    car_count = CartItem.objects.all().count()
    object_list =Product.objects.filter(Q(owner=user))

    context = {
        'user':user,
        'products':object_list,
        'cart_count':car_count,
    }
    return render(request,"profile.html",context)



class ShopView(ListView):
    model = Product
    template_name = 'shop.html'
# Getting context of Shop View
    def get_context_data(self, **kwargs):
        user = self.request.user
        object_list =Product.objects.all()
        # Call the base implementation first to get a context
        car_count = CartItem.objects.all().count()
        context = {
            'object_list':object_list,
            'cart_count':car_count,
        }
        return context
    

class SearchResultView(ListView):
    model = Product
    template_name = 'shop.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list =Product.objects.filter(
            Q(name=query) or Q(name=query)
        )
        return object_list

@method_decorator(login_required, name='dispatch')
class SellersView(ListView):
    model = Product
    template_name = 'sellingProducts.html'
    context_object_name = 'product'
   
    def get_context_data(self, **kwargs):
        user = self.request.user
        object_list =Product.objects.filter(Q(owner=user))
        # Call the base implementation first to get a context
        car_count = CartItem.objects.all().count()
        context = {
            'products':object_list,
            'cart_count':car_count
        }
        return context
     

@method_decorator(login_required,name='dispatch')
class UpdateProductView(UpdateView):
    model = Product
    template_name = 'UpdateProduct.html'
    fields = ['name' ,'owner' ,'detail' ,'discount' ,'image','quantity' ,'category']
    
    def form_valid(self, form):
        print("Working")
        return super().form_valid(form)

    def myproducts(request,slug): # new
        user = request.user
        object_list =Product.objects.filter(Q(slug=slug))    
        return object_list
    
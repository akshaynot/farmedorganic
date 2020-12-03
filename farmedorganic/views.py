from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView , CreateView , UpdateView , DeleteView , FormView
from django.db.models import Q # new
from products.models import Product
from django.contrib.auth.models import User
from .forms import ProductForm
# Create your views here.

def home(request):
    user = User
    products = Product.objects.all()

    context = {
        'products':products,
        'user':user,
    }
    return render(request,"home.html",context)

@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    context = {
        'user':user,
    }
    return render(request,"profile.html",context)

def CreateProduct(request):
    Pform = ProductForm 
    form = Pform(request.POST or None, request.FILES or None) 
    if form.is_valid:
        print(form.data['owner'])
    context = {
        'form' : Pform 
    }
    return render(request,"CreateProduct.html",context)



class ShopView(ListView):
    model = Product
    template_name = 'shop.html'

class SearchResultView(ListView):
    model = Product
    template_name = 'shop.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name=query) or Q(name=query)
        )
        return object_list
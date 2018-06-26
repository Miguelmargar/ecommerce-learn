from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

# Create your views here.

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    

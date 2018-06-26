from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Product
# Create your views here.

def view_cart(request):
    return render(request, "cart/viewcart.html")

def add_to_cart(request):
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    return HttpResponse()
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
# Create your views here.

def view_cart(request):
    return render(request, "cart/viewcart.html")

#the below adds a cart in session which is not permanent for the user - it's stored in memory
def add_to_cart(request):
    #get the product we are adding
    id = request.POST["product_id"]
    product = get_object_or_404(Product, pk=id)
    #get the current cart
    cart = request.session.get("cart", {})
    #update the cart
    # the below is a diccitionary and if non for the product it adds 1
    cart[id] = cart.get(id, 0) + 1
    #save cart
    request.session["cart"] = cart
    #redirect somewhere
    return HttpResponse(cart[id])    
    
    
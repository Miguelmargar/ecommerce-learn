from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
from .utils import get_cart_items_and_total
# Create your views here.

def view_cart(request):
    #the below creates a session in memory
    cart = request.session.get("cart", {})
    #the line below is a refactored line which long version is in .utils
    context = get_cart_items_and_total(cart)
        
    #the below renders the html page and gives the cart_items list to cart to be able to use cart in the html to loop through it
    return render(request, "cart/viewcart.html", context)

#the below adds a cart in session which is not permanent for the user - it's stored in memory
def add_to_cart(request):
    #get the product we are adding
    id = request.POST["product_id"]#product id here could be banana but has to be the same as in the html name tag
    product = get_object_or_404(Product, pk=id)
    #get the current cart
    cart = request.session.get("cart", {})
    #update the cart
    # the below is a diccitionary and if non for the product it adds 1
    cart[id] = cart.get(id, 0) + 1
    #save cart
    request.session["cart"] = cart
    #redirect somewhere
    return redirect("get_products")   
    
def remove_from_cart(request):
    id = request.POST["product_id"]#product id here could be banana but has to be the same as in the html name tag
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get("cart", {})
    if cart[id] > 1:
        cart[id] = cart.get(id, 0) - 1
    else:
        del cart[id]
    request.session["cart"] = cart
    return redirect("view_cart")
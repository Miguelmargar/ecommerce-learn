from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
# Create your views here.

def view_cart(request):
    #the below creates a session in memory
    cart = request.session.get("cart", {})
    cart_total = 0
    #the below loops through cart appends each product to the list created
    cart_items = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)
        quantity = cart[p]
        
        cart_item = {
          "product": product,
          "quantity": quantity,
          "sub_total": product.price * quantity
        }
        #the below apends all cart_item in the loop to the cart_items list created above the loop
        cart_items.append(cart_item)
        #the below adds all the sub_total(s) to cart_total variable created above which starts with 0
        cart_total += cart_item["sub_total"]
        
    #the below renders the html page and gives the cart_items list to cart to be able to use cart in the html to loop through it
    return render(request, "cart/viewcart.html", {"cart": cart_items, "cart_total": cart_total })

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
    
def remove_from_cart(request):
    id = request.POST["product_id"]
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get("cart", {})
    if cart[id] > 1:
        cart[id] = cart.get(id, 0) - 1
    else:
        del cart[id]
    request.session["cart"] = cart
    return redirect("view_cart")
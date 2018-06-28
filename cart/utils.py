from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):    
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

    return {"cart": cart_items, "cart_total": cart_total }
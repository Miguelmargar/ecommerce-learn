from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
#from decimal import Decimal
from cart.utils import get_cart_items_and_total
#from django.utils import timezone
from .models import OrderLineItem
#from django.contrib import messages
#from cart.utils import get_cart_items_and_total
#from .utils import save_order_items, charge_card, send_confirmation_email
#import stripe
from django.conf import settings


# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST, request.FILES)    
        payment_form = MakePaymentForm(request.POST, request.FILES)
        
        if order_form.is_valid():
            # Save The Order and payment_form.is_valid()
            order = order_form.save()
            #line below is not needed as we added auto_now_add=True in the date filed in the model therefore we do not need in the line above a commit="False" either- and do not need order.save() either as it is done in the line above too
            #order.date = timezone.now() 
            #order.save()
            cart = request.session.get('cart', {})
            #the below loops through product_id and quantity as cart.items() makes them a tuple.
            for product_id, quantity in cart.items():
                line_item = OrderLineItem()
                line_item.order = order
                line_item.product = get_object_or_404(Product, pk=product_id)
                line_item.quantity = quantity
                line_item.save()
            #below deletes cart from session when it is paid for    
            del request.session["cart"]      
        return HttpResponse("form sent")
    else:
        #this happens if it's a get and it shows the check page
        cart = request.session.get("cart", {})
        #refactoring used here again- this function is in cart.utils
        context = get_cart_items_and_total(cart)
         
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        forms =  {'order_form': order_form, 'payment_form': payment_form}
        #the below updates context variable with forms variable therefore can show context in the render at the  bottom
        context.update(forms)
        return render(request, "checkout/checkout.html", context)
    
    
        
        
        
     
        
    #         # Save the Order Line Items
            
    #         save_order_items(order, cart)
        
    #         # Charge the Card
    #         items_and_total = get_cart_items_and_total(cart)
    #         total = items_and_total['total']
    #         stripe_token=payment_form.cleaned_data['stripe_id']

    #         try:
    #             customer = charge_card(stripe_token, total)
    #         except stripe.error.CardError:
    #             messages.error(request, "Your card was declined!")

    #         if customer.paid:
    #             messages.error(request, "You have successfully paid")

    #             # Send Email
    #             send_confirmation_email(request.user.email, request.user, items_and_total)
        
    #             #Clear the Cart
    #             del request.session['cart']
    #             return redirect("home")
    # else:
       
        # cart_items_and_total = get_cart_items_and_total(cart)
        # context.update(cart_items_and_total)
    
    
    
    
    #'publishable': settings.STRIPE_PUBLISHABLE
from django.urls import path
from .views import get_products, add_to_cart

urlpatterns = [
    path('', get_products, name="get_products"),  
    path('cart/add', add_to_cart, name="add_to_cart")
]
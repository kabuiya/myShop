from django.contrib import admin

from .models import Products, Cart, CartItem, CustomerOrderDetails

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CustomerOrderDetails)
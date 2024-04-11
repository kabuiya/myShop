from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True)
    item_description = models.CharField(max_length=50, default='Default description')
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_amount = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Cart owned by {self.user}"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def cartitem_total(self):
        return self.product.price * self.quantity


class CustomerOrderDetails(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_address = models.CharField()
    customer_contact = models.IntegerField()
    customer_city = models.CharField()

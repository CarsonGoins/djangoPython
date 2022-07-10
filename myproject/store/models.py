from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product_set created by django

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='coll')


class Product(models.Model):
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
       Collection, on_delete=models.PROTECT
    )
    promotions = models.ManyToManyField(
        Promotion
    )

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE', 'Bronze'),
        ('MEMBERSHIP_SILVER', 'Silver'),
        ('MEMBERSHIP_GOLD', 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)


class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        ('PAYMENT_PENDING', 'Pending'),
        ('PAYMENT_COMPLETE', 'Complete'),
        ('PAYMENT_FAILED', 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT
    )
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT
    )
    product = models.ForeignKey(
       Product, on_delete=models.PROTECT 
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    zip = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #one-one relationship
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True) 
    #CASCADE makes it to where when a customer is deleted the associated address is deleted

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField()
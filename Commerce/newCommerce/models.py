from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model) :
    name= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class Cart(models.Model) :
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
      
    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartItem(models.Model) : 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=  models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.product.name} in Cart {self.cart.id}"


# Create your models here.


from django.contrib.auth.models import User
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    cover = models.ImageField(upload_to='slider_covers/')

class Service(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    bg = models.CharField(max_length=7)

class Product(models.Model):
    productName = models.CharField(max_length=255)
    imgUrl = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    shortDesc = models.TextField()
    description = models.TextField()
    avgRating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self): 
        return self.productName

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=55)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)



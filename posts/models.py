from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publish_year = models.IntegerField()
    pages = models.IntegerField()
    age = models.IntegerField()
    created_date = models.DateField(auto_now=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)



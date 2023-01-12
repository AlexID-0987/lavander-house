from django.db import models

# Create your models here.
class Products(models.Model):
    product=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='file/images')
    price=models.IntegerField()
    descriptions=models.CharField(max_length=150)
    
  

class Order(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    products=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    summa=models.PositiveIntegerField()
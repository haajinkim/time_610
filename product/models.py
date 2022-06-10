from django.db import models
# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "categorys"
    category =models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    
class Product(models.Model):
    class Meta:
        db_table = "product"
    name :models.CharField(max_length=128)
    category: models.ForeignKey(Category, on_delete=models.CASCADE)
    img :models. CharField(max_length=128)
    desc : models.CharField(max_length=128)
    price: models.IntegerField()
    count : models.ImageField()


class OrderStatus(models.Model):
    class Meta:
        db_table = "OrderStatus"
    status : models.CharField(max_length=128)
    payment : models.CharField(max_length=128)
    cancel : models.CharField(max_length=128)
    start_delivery: models.CharField(max_length=128)
    end_delivery: models.CharField(max_length=128)
    
class Productorder(models.Model):
    class Meta:
        db_table = "productorder"
    count: models.IntegerField()
    
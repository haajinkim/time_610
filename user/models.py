from django.db import models
from product.models import Productorder
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "user"
    count: models.IntegerField()

class User_orde(models.Model):
    class Meta:
        db_table = "User_orde"
    count = models.ForeignKey(Productorder, on_delete=models.CASCADE)
    address: models.CharField(max_length=128)
    order_time : models.IntegerField()
    all_price : models.IntegerField()
    approved_comment = models.BooleanField(default=True)



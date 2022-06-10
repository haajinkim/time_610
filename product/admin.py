from django.contrib import admin
from . models import Product,Category,OrderStatus,Productorder
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderStatus)
admin.site.register(Productorder)

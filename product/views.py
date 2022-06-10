from django.shortcuts import render
from . models import Product
# Create your views here.
def start(request):
    all = Product.objects.all()
    name = "hajin"
    category = "categry"
    price = "price"
    img = "img"
    desc = "desc"
    count ="count"
    all.save()
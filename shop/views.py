from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from datetime import datetime
from shop.models import Product


def all_products(request: HttpRequest):
    current_time = datetime.now()
    products = Product.objects.values_list('title', flat=True)
    return render(request, 'products.html', context={'current_time': current_time, 'products':products})




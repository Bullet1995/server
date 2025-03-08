from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from shop.models import Product


def all_products(request: HttpRequest):
    product_titles = Product.objects.values_list('title', flat=True)
    titles = b''
    for title in product_titles:
        titles += title.encode('utf-8') + b'\n'
    return HttpResponse(titles)


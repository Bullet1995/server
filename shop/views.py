from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime
from shop.models import Product
from shop.forms import CustomUserCreationForm


def all_products(request: HttpRequest):
    current_time = datetime.now()
    products = Product.objects.values_list('title', flat=True)
    return render(request, 'products.html', context={'current_time': current_time, 'products':products})


def register_page(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-products")
    form = CustomUserCreationForm()
    return render(request, 'registration.html', context={"form":form})

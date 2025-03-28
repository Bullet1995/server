from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views import View

from datetime import datetime

from django.views.generic import ListView, DetailView

from shop.models import Product
from shop.forms import CustomUserCreationForm, UserAuthForm
from shop.mixins import IsAuthenticatedMixin


class AllProductsView(IsAuthenticatedMixin, ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'

# def all_products(request: HttpRequest):
#     current_time = datetime.now()
#     products = Product.objects.values_list('title', flat=True)
#     return render(request, 'products.html', context={'current_time': current_time, 'products':products})

class LoginView(View):
    @staticmethod
    def get(request: HttpRequest):
        form = UserAuthForm()
        return render(request, "login.html", context={'form': form})

    @staticmethod
    def post(request: HttpRequest):
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('all-products')
            else:
                messages.error(request, "Неверное имя пользователя или пароль")
        else:
            messages.error(request, form.errors)

        form = UserAuthForm()
        return render(request, "login.html", context={'form': form})

class RegistrationView(View):
    @staticmethod
    def get(request: HttpRequest):
        form = CustomUserCreationForm()
        return render(request, 'registration.html', context={"form": form})

    @staticmethod
    def post(request: HttpRequest):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("all-products")
        form = CustomUserCreationForm()
        return render(request, 'registration.html', context={"form": form})

# def registration_view(request: HttpRequest):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("all-products")
#     form = CustomUserCreationForm()
#     return render(request, 'registration.html', context={"form":form})

# def login_page(request: HttpRequest):
#     if request.method == "POST":
#         form = UserAuthForm(request.POST)
#         if form.is_valid():
#             username =  form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('all-products')
#             else:
#                 messages.error(request, "Неверное имя пользователя или пароль")
#         else:
#             messages.error(request, form.errors)
#
#     form = UserAuthForm()
#     return render(request, "login.html", context={'form': form})

def logout_user(request: HttpRequest):
    logout(request)
    return redirect("all-products")

class ProductDetailView(IsAuthenticatedMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
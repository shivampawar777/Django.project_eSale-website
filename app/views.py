from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# Create your views here.
'''def home(request):
    return render(request, 'home.html', {})'''

'''def product_details(request):
    return render(request, 'product_details.html', {})'''


class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category="TW")
        bottomwear = Product.objects.filter(category="BW")

        return render(request, 'home.html', {'topwear':topwear, 'bottomwear':bottomwear})
    
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_details.html', {'product':product})

def mobile(request):
    return render(request, 'mobile.html', {})

def laptop(request):
    return render(request, 'laptop.html', {})

def topwear(request):
    return render(request, 'topwear.html', {})

def bottomwear(request):
    return render(request, 'bottomwear.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def address(request):
    return render(request, 'address.html', {})

def orders(request):
    return render(request, 'orders.html', {})

def changepassword(request):
    return render(request, 'changepassword.html', {})

def logout(request):
    return render(request, 'logout.html', {})

def add_to_cart(request):
    return render(request, 'cart.html', {})

def login(request):
    return render(request, 'login.html', {})

def registration(request):
    return render(request, 'registration.html', {})

def buy(request):
    return render(request, 'buy.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})
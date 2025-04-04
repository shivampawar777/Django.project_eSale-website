from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages


# Create your views here.
#(1)Home page view
class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category="TW")
        bottomwear = Product.objects.filter(category="BW")

        return render(request, 'home.html', {'topwear':topwear, 'bottomwear':bottomwear})
    
#(2)This is shows product details
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_details.html', {'product':product})

#(3)This view shows mobiles according to search
def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category="M").filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__gt=10000)

    return render(request, 'mobile.html', {'mobiles':mobiles})

#(4)This is customer registration view
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'registration.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations! User registered successfully.')
        
        #form = CustomerRegistrationForm()
        return render(request, 'registration.html', {'form':form})


def address(request):
    return render(request, 'address.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def orders(request):
    return render(request, 'orders.html', {})

def laptop(request):
    return render(request, 'laptop.html', {})

def topwear(request):
    return render(request, 'topwear.html', {})

def bottomwear(request):
    return render(request, 'bottomwear.html', {})

def add_to_cart(request):
    return render(request, 'cart.html', {})

def buy(request):
    return render(request, 'buy.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})
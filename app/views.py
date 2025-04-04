from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from app.models import Customer


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


#(5)This is customer profile view
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            cust = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            cust.save()
            messages.success(request, "Profile updated successfully!")

        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form':form, 'active': 'btn-primary'})
                                                    


#(6)This is customer address view
def address(request):
    cust_address = Customer.objects.filter(user=request.user)
    cust_address.delete()
    return render(request, 'address.html', {'cust_address':cust_address, 'active':'btn-primary'})



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
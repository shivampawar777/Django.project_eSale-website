from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
#(1)Home page view
class Home_Page(View):
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

#(5)This view is to logout current user
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

#(6)This is customer profile view
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form':form})
    
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
        return render(request, 'profile.html', {'form':form})
                                                    
#(7)This is customer address view
@login_required
def address(request):
    cust_address = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'cust_address':cust_address})

#(8)This view to add product to the cart.
@login_required
def add_to_cart(request):
    usr = request.user
    pid = request.GET.get('prod_id')
    product_id = Product.objects.get(id=pid)
    Cart(user=usr, product=product_id).save()
    messages.success(request, "Product added to the cart")
    
    return redirect('/show-cart/')

#(9)This is customer address view
@login_required
def show_cart(request):
    if request.user.is_authenticated:
        usr = request.user
        cart = Cart.objects.filter(user=usr)

        amount=0.0
        shipping_charges=50.0
        total_amount=0.0
        cart_products=[p for p in Cart.objects.all() if p.user == request.user]
        
        if cart_products:
            for p in cart_products:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                total_amount = amount + shipping_charges

            return render(request, 'show_cart.html', {'cart': cart, 'amount':amount,'shipping_charges':shipping_charges, 'total_amount':total_amount})
        else:
            return render(request, 'empty_cart.html')

#(10)This is customer address view
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()

        amount=0.0
        shipping_charges=50.0
        cart_products = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_products:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {'quantity':c.quantity, 'amount':amount, 'total_amount': amount+shipping_charges}
        return JsonResponse(data)
    else:
        return HttpResponse("")

#(11)This is customer address view
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()

        amount=0.0
        shipping_charges=50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {'quantity':c.quantity, 'amount':amount, 'total_amount':amount+shipping_charges}
        return JsonResponse(data)
    else:
        return HttpResponse("")

#(12)This is customer address view
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        
        amount=0.0
        shipping_charges=50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {'amount':amount, 'total_amount':amount+shipping_charges}
        return JsonResponse(data)
    else:
        return HttpResponse("")


#(13)This is checkout view
@login_required
def checkout(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cust_address = Customer.objects.filter(user=user)

    amount = 0.0
    shipping_amount = 50.0
    totalamount=0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        
        total_amount = amount+shipping_amount

    return render(request, 'checkout.html', {'cart_items':cart_items, 'cust_address':cust_address, 'total_amount':total_amount})

#(14)This is payment_done view
@login_required
def payment_done(request):
    cust_id = request.GET.get['custid']
    user = request.user
    customer = Customer.objects.get(id=cust_id)
    cart_id = Cart.objects.filter(user=user)

    for id in cart_id:
        OrderPlaced(user=user, customer=customer, product=id.product, quantity=id.quantity).save()
        id.delete()

    return redirect('/orders/')

#(15)This is orders view
@login_required
def orders(request):
    order_placed = OrderPlaced.object.get(user=request.user)

    return render(request, 'orders.html', {'order_placed':order_placed})



def buy(request):
    return render(request, 'buy.html', {})




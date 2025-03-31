from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('mobile/', mobile),
    path('laptop/', laptop),
    path('topwear/', topwear),
    path('bottomwear/', bottomwear),
    path('profile/', profile),
    path('address/', address),
    path('orders/', orders),
    path('changepassword/', changepassword),
    path('logout/', logout),
    path('add-to-cart/', add_to_cart),
    path('login/', login),
    path('registration/', registration),
    path('product-details/', product_details),
    path('buy/', buy),
    path('checkout/', checkout),
]



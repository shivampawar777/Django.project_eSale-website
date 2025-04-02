from django.urls import path
from .views import *

urlpatterns = [
    path('home/', ProductView.as_view()),
    path('product-details/<int:pk>/', ProductDetailsView.as_view()),
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
    path('buy/', buy),
    path('checkout/', checkout),
]



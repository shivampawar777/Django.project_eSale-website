from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('home/', ProductView.as_view()),
    path('product-details/<int:pk>/', ProductDetailsView.as_view()),
    path('mobile/', mobile),
    path('mobile/<slug:data>', mobile),
    path('registration/', CustomerRegistrationView.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm)),
    path('laptop/', laptop),
    path('topwear/', topwear),
    path('bottomwear/', bottomwear),
    path('profile/', profile),
    path('address/', address),
    path('orders/', orders),
    path('changepassword/', changepassword),
    path('logout/', logout),
    path('add-to-cart/', add_to_cart),
    path('buy/', buy),
    path('checkout/', checkout),
]



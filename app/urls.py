from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ChangePasswordForm, Password_Reset_Form, PasswordResetConfirmForm


urlpatterns = [
    path('home/', ProductView.as_view()),
    path('product-details/<int:pk>/', ProductDetailsView.as_view()),
    
    path('mobile/', mobile),
    path('mobile/<slug:data>', mobile),
    
    path('registration/', CustomerRegistrationView.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name="login"),

    path('logout/', auth_views.LogoutView.as_view()),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html', form_class=ChangePasswordForm, success_url='/changepassword-done/')),
    path('changepassword-done/', auth_views.PasswordChangeDoneView.as_view(template_name='changepassword-done.html')),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=Password_Reset_Form)),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=PasswordResetConfirmForm), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),


    path('profile/', ProfileView.as_view()),

    path('address/', address),


    path('laptop/', laptop),
    path('topwear/', topwear),
    path('bottomwear/', bottomwear),
    path('orders/', orders),
    path('add-to-cart/', add_to_cart),
    path('buy/', buy),
    path('checkout/', checkout),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.account, name="account"),
    path("about",views.about, name="about"),
    path("cart",views.cart, name="cart"),
    path("contact",views.contact, name="contact"),
    path("home",views.index, name="home"),
    path("account",views.account, name="accounts"),
    path("product-details",views.productDetails, name="product-details"),
    path("products",views.products, name="products"),
    path("reg", views.registration, name='registration'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),

    
]
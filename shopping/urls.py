"""machine_mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
home_view,
about,
contact,
register_service,
login,
logout,
register,
productview,
product_detailview,
catcegoryview,
addtocart,
cartview,
deletecartitem,
remove_cartitem_qty
)
app_name='shopping'
urlpatterns = [
    path('', home_view, name="home"),
    path('home', home_view,name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('register_service', register_service, name="register_service"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('addtocart/<slug>', addtocart, name="addtocart"),
    path('deletecartitem/<slug>', deletecartitem, name="deletecartitem"),
    path('remove_cartitem_qty/<slug>', remove_cartitem_qty, name="remove_cartitem_qty"),
    path('cart',cartview.as_view(), name="cart"),
    path('products',productview.as_view(), name="product"), #product view
    path('products/<slug>',catcegoryview.as_view(), name="productcat"), #category view
    path('products_detail/<slug>',product_detailview.as_view(), name="productsdet"),#productdetail view
]

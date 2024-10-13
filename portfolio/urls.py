from django.urls import path
from . import views 

urlpatterns=[
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),


]
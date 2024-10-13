from django.shortcuts import render

# Create your views here.


def index (request):

    return render (request, "portfolio/index.html")

def checkout (request):

    return render (request, "portfolio/checkout.html")

def cart (request):

    return render (request, "portfolio/cart.html")


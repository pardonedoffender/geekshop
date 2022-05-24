from django.shortcuts import render

from basketapp.models import Basket
from productapp.models import Product


def index(request):
    products = Product.objects.all()[:4]
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Магазин',
        'products': products,
        'basket': basket,
    }

    return render(request, 'geek_shop/index.html', context)


def contacts(request):
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'контакты',
        'basket': basket,
    }
    return render(request, 'geek_shop/contact.html', context)

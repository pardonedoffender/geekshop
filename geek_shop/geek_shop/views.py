from django.shortcuts import render

from productapp.models import Product


def index(request):
    products = Product.objects.all()[:4]

    context = {
        'title': 'Магазин',
        'products': products,
    }

    return render(request, 'geek_shop/index.html', context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'geek_shop/contact.html', context)

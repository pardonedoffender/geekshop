from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from productapp.models import ProductCategory, Product


def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'productapp/products_list.html', context)

    some_products = Product.objects.all()[2:5]
    context = {
        'title': title,
        'links_menu': links_menu,
        'some_products': some_products,
        'basket': basket,
    }
    return render(request, 'productapp/products.html', context=context)


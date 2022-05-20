from django.shortcuts import render

from productapp.models import Product


def products(request):
    links_menu = [
        {'href': '', 'name': 'все'},
        {'href': '', 'name': 'дом'},
        {'href': '', 'name': 'офис'},
        {'href': '', 'name': 'модерн'},
        {'href': '', 'name': 'классика'},
    ]
    context = {
        'title': 'Каталог',
        'links_menu': links_menu,
        # 'object': Product.objects.get(id=1)
    }
    return render(request, 'productapp/products.html', context)


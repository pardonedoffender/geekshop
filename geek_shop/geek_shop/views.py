from django.shortcuts import render


def index(request):
    return render(request, 'geek_shop/index.html')


def contacts(request):
    return render(request, 'geek_shop/contact.html')

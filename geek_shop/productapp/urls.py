from django.urls import path
from .views import products, product

app_name = 'productapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('<int:pk>/', product, name='details'),
]

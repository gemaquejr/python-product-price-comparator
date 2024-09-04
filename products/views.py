from django.shortcuts import render
from .models import Product, Price


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def price_comparison(request, product_id):
    product = Product.objects.get(id=product_id)
    prices = Price.objects.filter(product=product)
    return render(request, 'products/price_comparison.html', {'product': product, 'prices': prices})

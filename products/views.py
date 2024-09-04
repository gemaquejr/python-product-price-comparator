from django.shortcuts import render, redirect
from .models import Product, Price, Supermarket


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def add_product_page(request):
    products = Product.objects.all()
    supermarkets = Supermarket.objects.all()
    return render(request, 'products/add_product.html', {'products': products, 'supermarkets': supermarkets})


def price_comparison(request, product_id):
    product = Product.objects.get(id=product_id)
    prices = Price.objects.filter(product=product)
    return render(request, 'products/price_comparison.html', {'product': product, 'prices': prices})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        if name and category:
            Product.objects.create(name=name, description=description, category=category)
        return redirect('product_list')
    else:
        return redirect('add_product_page')


def add_price(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        supermarket_id = request.POST.get('supermarket')
        price = request.POST.get('price')
        if product_id and supermarket_id and price:
            product = Product.objects.get(id=product_id)
            supermarket = Supermarket.objects.get(id=supermarket_id)
            Price.objects.create(product=product, supermarket=supermarket, price=price)
        return redirect('product_list')
    else:
        return redirect('add_product_page')

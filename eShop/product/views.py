from django.shortcuts import render

from main.models import Category, Product, Image


def categoryProducts(request, category_slug):
    category = Category.objects.filter(slug=category_slug)
    products = Product.objects.filter(category__in=category)
    images = []
    for product in products:
        images.append(Image.objects.filter(product=product)[0])
    return render(request, 'product/category_products.html', {'context': zip(products, images)})

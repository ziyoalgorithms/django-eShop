from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator
import random

from main.models import Category, Product, Image


def categoryProducts(request, category_slug):
    category = Category.objects.filter(slug=category_slug)
    min_price = int(request.POST.get('minamount', '0'))
    max_price = int(request.POST.get('maxamount', '200000'))
    sort_opt = int(request.POST.get('sort_opt', '0'))
    sort_types = ['id', 'name', '-name', 'price', '-price']
    sort_types = {item: sort_types[item] for item in range(5)}

    products = Product.objects.filter(
        category__in=category,
        price__gte=min_price,
        price__lte=max_price,
    ).order_by(sort_types[sort_opt])

    images = []
    for product in products:
        images.append(Image.objects.filter(product=product)[0])
    list = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = list.get_page(page_number)

    context = {
        'title': category[0],
        'items': zip(page_obj, images),
        'page_obj': page_obj,
    }
    return render(request, 'product/category_products.html', context)


class ProductDetailView(DetailView):
    template_name = 'product/product-details.html'
    queryset = Product.objects.all()
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(category=context['object'].category)
        products = list(products)
        try:
            context['random_products'] = random.sample(products, 3)
        except:
            context['random_products'] = []
        context['title'] = 'Product Detail'
        return context


def search_product(request):
    query_name = request.GET.get('q', None)
    if query_name:
        products = Product.objects.filter(
            name__contains=query_name
        )

        images = []
        for product in products:
            images.append(Image.objects.filter(product=product)[0])
        list = Paginator(products, 12)
        page_number = request.POST.get('page')
        page_obj = list.get_page(page_number)

        context = {
            'items': zip(page_obj, images),
            'page_obj': page_obj,
        }
        return render(request, 'product/search_products.html', context)

    return render(request, 'product/search_products.html')

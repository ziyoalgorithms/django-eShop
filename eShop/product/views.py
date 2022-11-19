from django.shortcuts import render
from django.views.generic import DetailView

from main.models import Category, Product, Image


def categoryProducts(request, category_slug):
    category = Category.objects.filter(slug=category_slug)
    products = Product.objects.filter(category__in=category)
    images = []
    for product in products:
        images.append(Image.objects.filter(product=product)[0])

    context = {
        'items': zip(products, images),
        'title': category[0].name,
    }
    return render(request, 'product/category_products.html', context)


class ProductDetailView(DetailView):
    template_name = 'product/product-details.html'
    queryset = Product.objects.all()
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product Detail'
        return context

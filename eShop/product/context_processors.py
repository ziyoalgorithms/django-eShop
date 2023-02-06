import datetime
from django.contrib.sessions.models import Session

from main.models import Product


def recommendations(request):
    liked_products_ids = []
    try:
        for s in Session.objects.all():
            like = s.get_decoded()['like']
            if like:
                liked_products_ids.extend(like.keys())
    except:
        pass

    liked_products = Product.objects.filter(id__in=liked_products_ids)

    if liked_products.count() > 6:
        liked_products = liked_products[:6]

    return {'liked_products': liked_products}


def best_seller_products(request):
    products = Product.objects.all().order_by('count_sold')
    if products.count() > 6:
        products = products[:6]

    return {'bs_products': products}


def new_products(request):
    new_prods = Product.objects.filter(
        created_at__gte=datetime.datetime.now()-datetime.timedelta(30)
    )

    if new_prods.count() > 6:
        new_prods = new_prods[:6]

    return {'new_prods': new_prods}

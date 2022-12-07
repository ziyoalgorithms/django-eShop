from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from main.models import Product


def basket_summary(request):
    return render(request, 'basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        print(basketqty)
        return JsonResponse({'qty': basketqty})


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        return JsonResponse({'Success': True})

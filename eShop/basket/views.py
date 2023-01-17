from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .basket import Basket
from main.models import Product


@login_required(login_url=reverse_lazy('user:login'))
def basket_summary(request):
    basket = Basket(request)

    return render(request, 'basket/summary.html', {'basket': basket})


@login_required(login_url=reverse_lazy('user:login'))
def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        return JsonResponse({'qty': basketqty})


@login_required(login_url=reverse_lazy('user:login'))
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        return JsonResponse({'qty': basketqty, 'subtotal': baskettotal})


@login_required(login_url=reverse_lazy('user:login'))
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        return JsonResponse({'qty': basketqty, 'subtotal': baskettotal})

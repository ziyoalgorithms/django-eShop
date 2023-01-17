from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .like import Like
from main.models import Product


@login_required(login_url=reverse_lazy('user:login'))
def like_main(request):
    like = Like(request)

    return render(request, 'like/main.html', {'like': like})


@login_required(login_url=reverse_lazy('user:login'))
def like_add(request):
    like = Like(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        like.add(product=product)

        like_len = like.__len__()

        return JsonResponse({'like_len': like_len})


@login_required(login_url=reverse_lazy('user:login'))
def like_delete(request):
    like = Like(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        like.delete(product=product_id)

        like_len = like.__len__()

        return JsonResponse({'like_len': like_len})


@login_required(login_url=reverse_lazy('user:login'))
def like_clear(request):
    like = Like(request)
    if request.POST.get('action') == 'post':
        like.clear()
        return JsonResponse({})

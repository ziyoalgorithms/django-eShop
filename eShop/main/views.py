from django.shortcuts import render

from .models import Category


def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'main/home.html', context=context)

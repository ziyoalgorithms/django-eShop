from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Category, Product


class Home(TemplateView):
    template_name = 'main/home.html'

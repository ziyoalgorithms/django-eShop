from django.urls import path

from . import views


app_name = 'product'

urlpatterns = [
    path('<slug:category_slug>/', views.categoryProducts, name='category_products'),
]

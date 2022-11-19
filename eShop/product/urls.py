from django.urls import path

from . import views


app_name = 'product'

urlpatterns = [
    path('<slug:category_slug>/', views.categoryProducts, name='category_products'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetailView.as_view(), name='product_detail'),
]

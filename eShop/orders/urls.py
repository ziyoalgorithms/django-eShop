from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required

from orders.views import (
    OrderListView,
    order_create,
)

app_name = 'orders'

urlpatterns = [

    path('', login_required(
        OrderListView.as_view(),
        login_url=reverse_lazy('user:login')
    ), name='orders_list'),

    path('add/', order_create, name='order_create',)
]

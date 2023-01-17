from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from basket.basket import Basket
from orders.models import Order, OrderItem
from orders.forms import OrderForm, OrderItemForm


class OrderListView(ListView):
    model = OrderItem
    template_name = 'orders/orders_list.html'

    def get_queryset(self):
        orders = Order.objects.filter(user=self.request.user)
        return OrderItem.objects.filter(order__in=orders)


@login_required(login_url=reverse_lazy('users:login'))
def order_create(request):
    basket = Basket(request)
    order_form = OrderForm()
    if basket.__len__():
        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                new_order = order_form.save(commit=False)
                new_order.user = request.user
                new_order.save()
                for item in basket:
                    OrderItem.objects.create(
                        order=new_order,
                        product=item['product'],
                        price=item['total_price'],
                        quantity=item['qty']
                    )
                Basket(request).clear()
                messages.success(request, 'Buyurtmangiz qabul qilindi!')
                return HttpResponseRedirect(reverse('orders:orders_list'))

    else:
        messages.warning(request, "Savatingiz bo'sh!")
        return HttpResponseRedirect('/')

    return render(request, 'orders/order_form.html', {'form': order_form})

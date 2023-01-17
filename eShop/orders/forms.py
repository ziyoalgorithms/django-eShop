from django import forms

from orders.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=13,
        label='Telefon raqam',
        widget=forms.TextInput(),
    )
    city = forms.CharField(
        max_length=100,
        label='Viloyat',
        widget=forms.TextInput(),
    )
    full_adderss = forms.CharField(
        max_length=250,
        label="To'liq manzil",
        widget=forms.TextInput(),
    )

    class Meta:
        model = Order
        exclude = ('user', 'status')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'col-lg-12 col-md-6'


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'col-lg-12 col-md-6'

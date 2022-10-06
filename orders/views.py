from django.shortcuts import render
from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from .models import Order


def home(request):
    return render(request, 'orders/home.html')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm


def receipt(request):
    return render(request, 'orders/receipt.html')

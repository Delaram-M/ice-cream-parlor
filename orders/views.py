from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from .models import Order


def home_redirect(request):
    return redirect('orders:home')


def home(request):
    return render(request, 'orders/home.html')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        response = super(OrderCreateView, self).form_valid(form)
        self.request.session['customer_name'] = form.cleaned_data['customer_name']
        self.request.session['flavors'] = str([flavor.name for flavor in form.cleaned_data['flavors']])[1:-1]
        formatted_pickup_time = datetime.strptime(form.cleaned_data['pickup_time'],
                                                  "%Y-%m-%d %H:%M:%S.%f%z").strftime("%m/%d, %H:%M")
        self.request.session['pickup_time'] = formatted_pickup_time
        return response


def receipt(request):
    receipt_data = dict()
    for key, value in request.session.items():
        receipt_data[key] = value
    context = {'receipt_data': receipt_data}
    return render(request, 'orders/receipt.html', context)

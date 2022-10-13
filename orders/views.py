from django.shortcuts import render
from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from .models import Order


def home(request):
    return render(request, 'orders/home.html')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        response = super(OrderCreateView, self).form_valid(form)
        self.request.session['customer_name'] = str(form.cleaned_data['customer_name'])
        self.request.session['flavors'] = str([flavor.name for flavor in form.cleaned_data['flavors']])[1:-1]
        self.request.session['pickup_time'] = str(form.cleaned_data['pickup_time'])[5:16]
        return response


def receipt(request):
    receipt_data = dict()
    for key, value in request.session.items():
        receipt_data[key] = value
    context = {'receipt_data': receipt_data}
    return render(request, 'orders/receipt.html', context)

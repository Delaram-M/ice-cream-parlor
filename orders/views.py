import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from orders.forms import OrderForm
from .models import Flavor


def home(request):
    return render(request, 'orders/home.html')


def order(request):
    flavors = Flavor.objects.all()
    order_form = OrderForm()
    context = {'flavors': flavors, 'order_form': order_form}
    return render(request, 'orders/order.html', context)


def submit(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        pickup_in = form['pickup_in']
        form = form.save(commit=False)
        form.pickup_time = timezone.now() + datetime.timedelta(minutes=int(pickup_in.value()))
        form.save()
        return HttpResponseRedirect(reverse('orders:receipt'))
    else:
        return HttpResponseRedirect(reverse('orders:submit'))


def receipt(request):
    return render(request, 'orders/receipt.html')

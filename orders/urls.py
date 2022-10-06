from django.urls import path, reverse_lazy

from . import views
from .views import OrderCreateView

app_name = 'orders'
urlpatterns = [
    path('', views.home, name='home'),
    path('order/create', OrderCreateView.as_view(success_url=reverse_lazy('orders:receipt')), name='order_create'),
    path('receipt', views.receipt, name='receipt')
]

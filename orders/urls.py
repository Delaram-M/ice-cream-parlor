from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('submit', views.submit, name='submit'),
    path('receipt', views.receipt, name='receipt')
]

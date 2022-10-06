from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('orders.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
]

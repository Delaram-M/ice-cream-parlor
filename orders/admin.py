from django.contrib import admin

from .models import Flavor, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'pickup_time')
    list_filter = ['pickup_time']
    search_fields = ['customer_name']


admin.site.register(Flavor)
admin.site.register(Order, OrderAdmin)

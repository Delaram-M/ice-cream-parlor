from django.contrib import admin

from .models import Flavor, Order, PrepDuration


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'pickup_time')
    list_filter = ['pickup_time']
    search_fields = ['customer_name']


class PrepDurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration')


admin.site.register(Flavor)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrepDuration, PrepDurationAdmin)

from django.forms import ModelForm, ChoiceField, SelectMultiple

from orders.models import Order, Flavor

PREP_CHOICES = (
    (15, '15 minutes'),
    (30, '30 minutes'),
    (60, '1 hour')
)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['pickup_time']
        widgets = {
            'flavors': SelectMultiple(attrs={'size': len(Flavor.objects.all())}),
        }
    pickup_in = ChoiceField(choices=PREP_CHOICES)


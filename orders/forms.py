from django.forms import ModelForm, ChoiceField, SelectMultiple
from django.utils import timezone

from orders.models import Order, Flavor, PrepDuration


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'flavors': SelectMultiple(attrs={'size': len(Flavor.objects.all())}),
        }

    prep_durations = PrepDuration.objects.values_list('duration', flat=True)
    pickup_choices = [timezone.now() + delta for delta in prep_durations]
    pickup_tuple = tuple(zip(pickup_choices, [choice.strftime("%m/%d, %H:%M") for choice in pickup_choices]))
    pickup_time = ChoiceField(choices=pickup_tuple)

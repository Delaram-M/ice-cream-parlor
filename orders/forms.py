import datetime

from django.forms import ModelForm, ChoiceField, SelectMultiple
from django.utils import timezone

from orders.models import Order, Flavor, PrepDuration

# TODO move to DB
PREP_CHOICES = [15, 30, 60]


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'flavors': SelectMultiple(attrs={'size': len(Flavor.objects.all())}),
        }

    prep_durations = PrepDuration.objects.all()
    pickup_choices = [timezone.now() + datetime.timedelta(minutes=delta) for delta in PREP_CHOICES]
    pickup_tuple = tuple(zip(pickup_choices, [choice.strftime("%m/%d, %H:%M") for choice in pickup_choices]))
    pickup_time = ChoiceField(choices=pickup_tuple)

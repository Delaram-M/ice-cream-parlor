from django.db import models


class Flavor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PrepDuration(models.Model):
    duration = models.DurationField()

    class Meta:
        ordering = ['duration']

    def __str__(self):
        return str(self.duration)


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    flavors = models.ManyToManyField(Flavor)
    pickup_time = models.DateTimeField()

    class Meta:
        ordering = ['pickup_time']

    def __str__(self):
        return str(self.customer_name)

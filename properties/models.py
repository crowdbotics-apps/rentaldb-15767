from django.conf import settings
from django.db import models


class Address(models.Model):
    "Generated Model"
    street = models.CharField(max_length=100,)
    city = models.CharField(max_length=50,)
    state = models.CharField(max_length=30,)
    zip = models.DecimalField(max_digits=5, decimal_places=0,)


class Unit(models.Model):
    "Generated Model"
    address = models.ForeignKey(
        "properties.Address", on_delete=models.CASCADE, related_name="unit_address",
    )
    unitNum = models.CharField(max_length=6,)
    bed = models.DecimalField(max_digits=2, decimal_places=1,)
    bath = models.DecimalField(max_digits=2, decimal_places=1,)


# Create your models here.

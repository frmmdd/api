from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Store(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Deal(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
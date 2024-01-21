from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse("get_item", args=[self.pk])

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def get_absolute_url(self):
        return reverse("get_order", args=[self.pk])

# models.py

from django.conf import settings
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    brand = models.CharField(max_length=200)
    quality = models.CharField(max_length=50)
    imported_date = models.DateTimeField(default=timezone.now)
    sold_date = models.DateTimeField(blank=True, null=True)

    def sell(self):
        self.sold_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

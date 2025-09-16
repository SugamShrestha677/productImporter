from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True, help_text="Unique Stock Keeping Unit") # (sku)=Stock Keeping Unit
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
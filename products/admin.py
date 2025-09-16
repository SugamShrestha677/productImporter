from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('sku', 'name', 'price', 'quantity', 'added_on')
    search_fields = ('sku', 'name', 'description')
    list_filter = ('added_on',)
    readonly_fields = ('added_on',)
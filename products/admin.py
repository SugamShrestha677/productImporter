from django.contrib import admin

# Register your models here.
# products/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('sku', 'name', 'price', 'quantity', 'added_on')
    
    # Fields to search by
    search_fields = ('sku', 'name', 'description')
    
    # Fields to filter by
    list_filter = ('added_on',)
    
    # Fields that are read-only
    readonly_fields = ('added_on',)
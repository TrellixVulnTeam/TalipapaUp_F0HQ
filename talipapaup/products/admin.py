from django.contrib import admin

from .models import Product, Category,Stall

class ProductModel(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    
admin.site.register(Product, ProductModel)
admin.site.register(Category)
admin.site.register(Stall)
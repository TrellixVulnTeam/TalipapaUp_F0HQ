from django import forms
from .models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['mainimage','name', 'stall_address', 'category', 'preview_text', 'detail_text', 'price', 'measurement']
        
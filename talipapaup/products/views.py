from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import ProductsForm
from .models import Product
from .filters import ProductFilter


class ProductHome(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
def ProductDetail(request , product_id):
    obj = get_object_or_404(Product, product_id=product_id)
    template_name = "product/detail.html"
    context = {"detail" : obj}
    return render(request, template_name, context)

class Product_Addition(CreateView):
    model = Product
    form_class = ProductsForm
    success_url = reverse_lazy('products:list_of_product')
    template_name = 'product/create.html'




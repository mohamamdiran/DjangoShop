from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product, category


class product_detail(DetailView):
    template_name = 'Product/product_detail.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(product_detail,self).get_context_data(*args, **kwargs)
        context["AllCategories"] = category.objects.all()
        context["DisplayCategories"] = category.objects.filter(AddToListCategory = True)  
        return context

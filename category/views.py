from django.shortcuts import render
from django.views.generic import DetailView
from Product.models import category, Product
from django.shortcuts import get_object_or_404


class DetailCategory(DetailView):
    template_name = 'category/category_detail.html'
    model = category

    def get_object(self):
        pk = self.kwargs['pk']
        return category.objects.get(pk = pk)
        
    def get_context_data(self, *args, **kwargs):
        context = super(DetailCategory,self).get_context_data(*args, **kwargs)
        context["AllCategories"] = category.objects.all()
        context["DisplayCategories"] = category.objects.filter(AddToListCategory = True)  
        return context

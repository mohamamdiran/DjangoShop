from django.contrib import admin
from .models import Product, category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Slug','Description','Price')


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Slug','AddToTop','AddToListCategory')
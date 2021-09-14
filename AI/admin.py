from django.contrib import admin
from .models import DisplayedProducts


@admin.register(DisplayedProducts)
class DisplayedProductsAdmin(admin.ModelAdmin):
    list_display = ('id','User','Product')

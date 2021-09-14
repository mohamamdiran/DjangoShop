from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class DisplayedProducts(models.Model):
    User = models.ForeignKey(User,related_name="DisplayedProductsUser", on_delete=models.CASCADE)
    Product = models.TextField(verbose_name="List Of Product Id Number")
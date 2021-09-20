from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from datetime import datetime, timezone , timedelta

class Product(models.Model):
    # Fields Without Relationship
    Name = models.CharField(max_length=155)
    Image = models.ImageField(upload_to="ProductImages/")
    Slug = extension_fields.AutoSlugField(populate_from='Name', blank=True)
    Description = models.TextField(max_length=250)
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    # Relationship Fields
    Category = models.ManyToManyField(
        'Category', 
        related_name='Category'
    )
    Date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return u'%s' % self.Slug

    def get_absolute_url(self):
        return reverse('product_manager_product_detail', args=(self.Slug,))

    def get_update_url(self):
        return reverse('product_manager_product_update', args=(self.Slug,))

    def get_delete_url(self):
        return reverse('product_manager_product_delete', args=(self.Slug,))

    def get_short_description(self):
        if len(self.description) > 40 :
            return self.description[0:30] + '....'
        else:
            return self.description
    
    def IsNewProduct(self):
        if datetime.now().astimezone() < (self.Date +  timedelta(days=7)):
            return True
        else:
            return False

class category(models.Model):
    Name = models.CharField(max_length=155)
    Slug = extension_fields.AutoSlugField(populate_from='Name', blank=True)
    Image = models.ImageField(upload_to="CategoryImage/")
    AddToTop = models.BooleanField(default=False)
    AddToListCategory = models.BooleanField(default=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.Name

    def __unicode__(self):
        return u'%s' % self.Slug

    def get_absolute_url(self):
        return reverse('product_manager_category_detail', args=(self.Slug,))

    def get_update_url(self):
        return reverse('product_manager_category_update', args=(self.Slug,))

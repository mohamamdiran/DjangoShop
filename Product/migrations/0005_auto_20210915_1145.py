# Generated by Django 3.1.6 on 2021-09-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_category_addtolistcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ManyToManyField(related_name='Category', to='Product.category'),
        ),
    ]
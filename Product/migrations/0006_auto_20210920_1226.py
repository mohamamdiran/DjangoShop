# Generated by Django 3.1.6 on 2021-09-20 07:56

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20210915_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='Name'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-09-13 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.TextField(verbose_name='List Of Product Id Number')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DisplayedProductsUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

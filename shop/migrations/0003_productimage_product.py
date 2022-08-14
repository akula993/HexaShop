# Generated by Django 4.1 on 2022-08-14 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_productimage_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='product', to='shop.product', verbose_name='Продукт'),
        ),
    ]
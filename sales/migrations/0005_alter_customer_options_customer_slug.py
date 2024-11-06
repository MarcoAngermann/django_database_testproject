# Generated by Django 5.1.2 on 2024-11-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_bill_product_order_producttype_order_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]

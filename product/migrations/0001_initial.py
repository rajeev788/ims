# Generated by Django 5.0.2 on 2024-02-13 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=300)),
                ('category_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=300)),
                ('supplier_contact', models.IntegerField()),
                ('supplier_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_description', models.TextField()),
                ('product_unit_price', models.IntegerField()),
                ('quatity_on_hand', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='Product_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_in', models.IntegerField()),
                ('product_out', models.IntegerField()),
                ('opening_numbers_of_product', models.IntegerField()),
                ('closing_number_of_products', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('product_name', models.CharField(max_length=300)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.suppliers')),
            ],
        ),
    ]

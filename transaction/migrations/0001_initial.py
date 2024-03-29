# Generated by Django 5.0.2 on 2024-02-13 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('sales', 'sales'), ('purchase', 'purchase')], max_length=300)),
                ('transaction_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_transaction_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('notes', models.TextField(null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.inventory_transaction')),
            ],
        ),
    ]

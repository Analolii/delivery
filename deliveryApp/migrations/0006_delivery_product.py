# Generated by Django 5.1.3 on 2024-11-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryApp', '0005_rename_client_id_delivery_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='Product', through='deliveryApp.DeliveryProduct', to='deliveryApp.product'),
        ),
    ]

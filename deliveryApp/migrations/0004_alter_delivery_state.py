# Generated by Django 5.1.3 on 2024-11-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryApp', '0003_alter_deliveryproduct_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='state',
            field=models.CharField(choices=[('new', 'создана'), ('in_work', 'передана на доставку'), ('end', 'товар доставлен')], max_length=15),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-10 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0002_rename_fooditems_fooditem_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfooditem',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_items', to='foodDelivery.fooditem'),
        ),
    ]

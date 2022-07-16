# Generated by Django 4.0.6 on 2022-07-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0004_alter_orderfooditem_food_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='food_items',
            field=models.ManyToManyField(related_name='orders', through='foodDelivery.OrderFoodItem', to='foodDelivery.fooditem'),
        ),
        migrations.AlterField(
            model_name='orderfooditem',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodDelivery.fooditem'),
        ),
        migrations.AlterField(
            model_name='orderfooditem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodDelivery.order'),
        ),
    ]

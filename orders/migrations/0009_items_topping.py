# Generated by Django 3.0.7 on 2020-06-24 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Topping',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]

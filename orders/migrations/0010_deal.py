# Generated by Django 3.0.7 on 2020-06-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_items_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]

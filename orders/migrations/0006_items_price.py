# Generated by Django 3.0.7 on 2020-06-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200619_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
    ]

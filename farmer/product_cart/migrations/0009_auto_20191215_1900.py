# Generated by Django 2.0.3 on 2019-12-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0008_auto_20191215_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product_cart.OrderItem'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-12-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_page', '0009_auto_20191209_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.CharField(default='farmer@farmer.nl', max_length=30),
        ),
    ]

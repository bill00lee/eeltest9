# Generated by Django 2.0.3 on 2018-03-21 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='timestamp',
        ),
    ]

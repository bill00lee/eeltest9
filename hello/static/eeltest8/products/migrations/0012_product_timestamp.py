# Generated by Django 2.0.3 on 2018-03-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

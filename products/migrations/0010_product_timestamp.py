# Generated by Django 2.0.3 on 2018-03-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180313_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]

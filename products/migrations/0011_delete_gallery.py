# Generated by Django 3.1.2 on 2020-11-17 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
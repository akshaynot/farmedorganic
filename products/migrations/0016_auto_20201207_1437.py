# Generated by Django 3.1.2 on 2020-12-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20201207_1436'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductReview',
            new_name='Rating',
        ),
    ]
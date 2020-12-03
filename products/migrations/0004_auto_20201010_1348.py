# Generated by Django 3.1.2 on 2020-10-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201010_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, upload_to='Products')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='products.Gallery'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=100)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

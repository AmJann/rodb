# Generated by Django 4.1.5 on 2023-01-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rod', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='name',
            field=models.CharField(max_length=101),
        ),
    ]

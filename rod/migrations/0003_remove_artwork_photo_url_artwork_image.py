# Generated by Django 4.1.5 on 2023-02-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rod', '0002_alter_artwork_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/'),
        ),
    ]

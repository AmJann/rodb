# Generated by Django 4.1.5 on 2023-01-24 18:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=100)),
                ('subtype', models.CharField(max_length=100, null=True)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
    ]
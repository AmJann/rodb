from django.db import models
import uuid

class Artwork(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=101)
    size = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/", max_length=255)
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=20)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, null=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

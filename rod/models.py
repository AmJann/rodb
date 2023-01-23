from django.db import models

class Artwork(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = model.TextField()
    price = models.IntgerField()
    type = models.CharField()

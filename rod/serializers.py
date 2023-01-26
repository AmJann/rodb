from rest_framework import serializers
from .models import Artwork

class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artwork
        fields = ('uuid','name','size', 'photo_url', 'description', 'price', 'type', 'subtype', 'sold')
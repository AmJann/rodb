from django.shortcuts import render

from .models import Artwork
from rest_framework import generics, permissions
from .serializers import ArtworkSerializer

class Artworks(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

class ArtworksProtected(generics.ListAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer    

    permission_classes = [permissions.IsAuthenticated]

class ArtworkCreateProtected(generics.CreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer  
    
    permission_classes = [permissions.IsAuthenticated]

class ArtworkDetailProtected(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all()

    permission_classes = [permissions.IsAuthenticated]


def Artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, 'home.html', {'artworks': artworks})    

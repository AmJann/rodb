from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Artwork
from rest_framework import generics, permissions
from .serializers import ArtworkSerializer

from .forms import ArtworkForm

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

def add_artwork(request):
    submitted = False
    if request.method == "POST":
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            form = ArtworkForm
            if submitted in request.GET:
                submitted = True  
    form = ArtworkForm
    return render(request, 'add_artwork.html', {'form': form, 'submitted': submitted}) 
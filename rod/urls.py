from django.urls import path
from . import views

urlpatterns = [
    path('artworks/', views.Artworks.as_view(), name ='artworks'),
    path('artworks_protected/', views.ArtworksProtected.as_view(), name ='artworks'),
    path('artwork_create/', views.ArtworkCreateProtected.as_view(), name='artwork_create'),
    path('artwork_detail/<uuid:pk>/', views.ArtworkDetailProtected.as_view(), name='artwork_detail'),
    path('artwork_edit/<uuid:pk>/', views.ArtworkDetailProtected.as_view(), name='artwork_edit'),
    path('artwork_delete/<uuid:pk>/', views.ArtworkDetailProtected.as_view(), name='artwork_delete'),
    path('', views.Artwork_list, name='artworks'),
    path('add_artwork', views.add_artwork,name='add-artwork'),
    
]
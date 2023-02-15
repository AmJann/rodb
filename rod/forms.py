from django import forms
from django.forms import ModelForm
from .models import Artwork


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ('name','size','description','price','type','subtype','image','sold')

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'size':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class': 'form-control'}),
            'type':forms.TextInput(attrs={'class': 'form-control'}),
            'subtype':forms.TextInput(attrs={'class': 'form-control'}),
            'image':forms.FileInput(attrs={'class': 'form-control-file'}),
        }
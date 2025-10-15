from django import forms
from .models import Publicacion


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            'titulo',
            'resumen',
            'contenido',
            'fk_categoria',
            'fk_estatu',
            'fk_foto_portada',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'fk_categoria': forms.Select(attrs={'class': 'form-select'}),
            'fk_estatu': forms.Select(attrs={'class': 'form-select'}),
            'fk_foto_portada': forms.Select(attrs={'class': 'form-select'}),
        }

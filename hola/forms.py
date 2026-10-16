from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Escribe el título aquí',
                'style': 'width: 100%; padding: 8px; margin: 5px 0;'
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Escribe el contenido aquí',
                'rows': 6,
                'style': 'width: 100%; padding: 8px; margin: 5px 0;'
            }),
        }

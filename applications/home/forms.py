from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = ('titulo','subtitulo','cantidad',)
        widgets = {
            'titulo' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese texto aquí',
                }
            ),
            'subtitulo' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ingrese un subtitulo aquí',
                }
            )
            
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')

        return cantidad
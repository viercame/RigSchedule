from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.forms import ModelForm, forms
from django.forms.widgets import DateInput, SelectDateWidget, TextInput, Widget
from intervenciones.models import Intervencion, Rig


ACTIVIDAD_CHOICES = [
    ('ABANDONO', 'Abandono'),
    ('WELLSERVICE', 'WS'),
    ('WORKOVER', 'WO'),
    ('REGISTRO', 'REGISTRO'),    
    ('EXTERNO', 'EXTERNO'),    
]

RECURSO_CHOICES = [
    ('CAPEX', 'CAPEX'),
    ('OPEX', 'OPEX'),
    ('ABEX', 'ABEX'),
]



class IntervencionForm(ModelForm):
    class Meta: 
        model = Intervencion
        fields = '__all__'
        widgets = {
            'inicio' : DateInput(attrs = {'type': 'text'}),
            'fin' : DateInput(attrs = {'type': 'text'}),
            'entradaproduccion' : DateInput(attrs = {'type': 'text'}),
            #'actividad' : forms.CharField('Selecciona la actividad', Widget=forms.Select(choices=ACTIVIDAD_CHOICES)),
            #'recurso' : forms.CharField('Selecciona el recurso', Widget=forms.Select(choices=RECURSO_CHOICES))

        }


class RigForm(ModelForm):
    class Meta: 
        model = Rig
        fields = '__all__'
        widgets = {
            'potencia' : TextInput(attrs = {'type': 'number'})
        }

from django import forms
from rlcms.apps.clientes.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'codigo',
            'tipo_cliente',
            'nombre',
            'domicilio',
        ]
        labels = {
            'codigo': 'Codigo del cliente',
            'tipo_cliente': 'Tipo de cliente',
            'nombre': 'Nombre',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
        }

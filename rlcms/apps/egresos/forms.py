from django import forms
from rlcms.apps.egresos.models import Egreso


class EgresoForm(forms.ModelForm):

    class Meta:
        model = Egreso
        fields = [
            'empleado',
            'unidad_medida',
            'descripcion',
            'costo_unitario',
            'cantidad',
            'fecha',
        ]
        labels = {
            'empleado': 'Empleado',
            'unidad_medida': 'Unidad de medida',
            'descripcion': 'Descripcion',
            'costo_unitario': 'Costo unitario',
            'cantidad': 'Cantidad',
            'fecha': 'Fecha',
        }
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }

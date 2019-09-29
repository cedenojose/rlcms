from django import forms
from rlcms.apps.pedidos.models import Factura, Credito

class FacturaForm(forms.ModelForm):

	class Meta:
		model = Factura
		fields = [
			'empleado',
			'cliente',
			'tipo_pago',
			'impuesto',
			'producto',
		]
		labels = {
			'empleado': 'Empleado',
			'cliente': 'Cliente',
			'tipo_pago': 'Tipo de pago',
			'impuesto': 'Impuesto',
			'producto': 'Producto',
		}
		widgets = {
			'empleado': forms.Select(attrs={'class': 'form-control'}),
			'cliente': forms.Select(attrs={'class': 'form-control'}),
			'tipo_pago': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
			'impuesto': forms.Select(attrs={'class': 'form-control'}),
			'producto': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
		}

class CreditoForm(forms.ModelForm):

	class Meta:
		model = Factura
		fields = [
			'factura',
			'fecha',
			'cancelado',
		]
		labels = {
			'factura': 'Factura',
			'fecha': 'Fecha',
			'cancelado': 'Cancelado',
		}
		widgets = {
			'Factura': forms.Select(attrs={'class': 'form-control'}),
			'fecha': forms.Select(attrs={'class': 'form-control'}),
			'cancelado': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
		}
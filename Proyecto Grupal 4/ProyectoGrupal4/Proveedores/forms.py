# se debe importar forms
from django import forms

# se debe importar el modelo creado anterirormente
from .models import Proveedores


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['rut_proveedor', 'nombre_proveedor', 'nombre_representante', 'telefono', 'comuna', 'direccion']

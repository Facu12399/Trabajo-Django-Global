from django import forms
from .models import Productos, Categoria

class FormProducto(forms.ModelForm):
    class Meta:
        error = "Errors found in the form"
        model = Productos
        exclude = []
        fields = '__all__'
        error_messages = {"error":error}
        
class FormCategoria(forms.ModelForm):
    class Meta:
        error = "Errors found in the form"
        model = Categoria
        exclude = []
        fields = '__all__'
        error_messages = {"error":error}
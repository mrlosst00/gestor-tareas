from django import forms
from .models import Task # Importamos el modelo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # Le decimos que este formulario es para el modelo Task

        # Definimos los campos que SÍ queremos que el usuario llene
        fields = ['title', 'status']

        # (No incluimos 'project' porque lo asignaremos automáticamente)
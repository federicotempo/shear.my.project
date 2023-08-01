from . import models
from django import forms


class ProyectoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProyectoCategoria
        fields = "__all__"


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = "__all__"

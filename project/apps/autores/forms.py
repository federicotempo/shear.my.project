from . import models
from django import forms

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = "__all__"

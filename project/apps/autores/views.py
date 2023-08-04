from django.shortcuts import render, redirect, get_object_or_404
from ast import Delete
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from . import models
from . import forms

#! Autor
# List


class AutorList(ListView):
    model = models.Autor

# INDEX


def index(request):
    return render(request, "autores/index.html")


# Create
class AutorCreate(CreateView):
    model = models.Autor
    form_class = forms.AutorForm
    success_url = reverse_lazy("autor:autor_list")

# Delete


class AutorDelete(DeleteView):
    model = models.Autor
    success_url = reverse_lazy("autor:autor_list")


# Modificar

def modificar_autor(request, id):
    autor = get_object_or_404(models.Autor, id=id)
    data = {
        'form': forms.AutorForm(instance=autor)
    }

    if request.method == 'POST':
        formulario = forms.AutorForm(
            data=request.POST, instance=autor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="autor:autor_list")
        data["form"] = formulario

    return render(request, "autores/autor_modificar.html", data)

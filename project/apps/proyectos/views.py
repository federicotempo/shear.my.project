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

#! ProyectoCategoria
# List


class ProyectoCategoriaList(ListView):
    model = models.ProyectoCategoria

# Create


class ProyectoCategoriaCreate(CreateView):
    model = models.ProyectoCategoria
    form_class = forms.ProyectoCategoriaForm
    success_url = reverse_lazy("proyectos:proyectocategoria_list")

# Delete


class ProyectoCategoriaDelete(DeleteView):
    model = models.ProyectoCategoria
    success_url = reverse_lazy("proyectos:proyectocategoria_list")


#! Proyectos
# List

class ProyectoList(ListView):
    model = models.Proyecto

# Create


class ProyectoCreate(CreateView):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    success_url = reverse_lazy("proyectos:proyecto_list")


# Delete
class ProyectoDelete(DeleteView):
    model = models.Proyecto
    success_url = reverse_lazy("proyectos:proyecto_list")

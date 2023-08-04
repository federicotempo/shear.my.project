from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
)

from . import models
from . import forms
from django.shortcuts import render, redirect, get_object_or_404

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


# Modificar

def modificar_proyectocategoria(request, id):
    proyecto = get_object_or_404(models.ProyectoCategoria, id=id)
    data = {
        'form': forms.ProyectoCategoriaForm(instance=proyecto)
    }

    if request.method == 'POST':
        formulario = forms.ProyectoCategoriaForm(
            data=request.POST, instance=proyecto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="proyectos:proyectocategoria_list")
        data["form"] = formulario

    return render(request, "proyectos/proyectocategoria_modificar.html", data)


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

# Modificar


def modificar_proyecto(request, id):
    proyecto = get_object_or_404(models.Proyecto, id=id)
    data = {
        'form': forms.ProyectoForm(instance=proyecto)
    }

    if request.method == 'POST':
        formulario = forms.ProyectoForm(
            data=request.POST, instance=proyecto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="proyectos:proyecto_list")
        data["form"] = formulario

    return render(request, "proyectos/proyecto_modificar.html", data)


# INDEX CATEGORIAS
def index_categoria(request):
    return render(request, "proyectos/index_categoria.html")

# INDEX PROYECTOS


def index_proyecto(request):
    return render(request, "proyectos/index_proyecto.html")

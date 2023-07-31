from . import models
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class ProyectoCategoriaList(ListView):
    model = models.ProyectoCategoria


class ProyectoList(ListView):
    model = models.Proyecto

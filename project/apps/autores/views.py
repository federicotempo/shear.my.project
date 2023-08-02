from django.shortcuts import render
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

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

#! Autor
# List


class AutorList(ListView):
    model = models.Autor

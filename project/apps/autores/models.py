from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Usuario


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Autores"
        verbose_name_plural = "Autores"

from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Usuario


class Usuario(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="usuario")
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.usuario.username

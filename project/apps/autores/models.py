from django.db import models
from django_countries.fields import CountryField
from django.utils.safestring import mark_safe

# Usuario


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    edad = models.PositiveIntegerField(null=True)
    telefono = models.PositiveIntegerField(null=True)
    pais = CountryField(verbose_name="país", null=True)
    avatar = models.ImageField(upload_to="avatares", null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.avatar.url))

    @property
    def get_photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/media/imagenes/default.png"

    class Meta:
        verbose_name = "Autores"
        verbose_name_plural = "Autores"

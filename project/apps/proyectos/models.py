from django.db import models
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from django.utils import timezone

# Categoria de los proyectos


class ProyectoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, verbose_name="descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "categoría de proyectos"
        verbose_name_plural = "categoría de proyectos"

# Proyectos


class Proyecto(models.Model):
    categoria_id = models.ForeignKey(
        ProyectoCategoria, on_delete=models.SET_NULL, null=True, verbose_name="Categoría")
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")
    opciones = (('En proceso', 'En proceso'), ('Finalizado', 'Finalizado'))
    estado = models.CharField(max_length=100, choices=opciones)
    autor_id = models.ForeignKey(
        "autores.Autor", on_delete=models.SET_NULL, null=True, verbose_name="Autor")
    ubicacion = CountryField(verbose_name="Ubicación", null=True)
    fecha_publicacion = models.DateTimeField(
        default=timezone.now, editable=False, null=True, verbose_name="Fecha de publicación")
    imagen = models.ImageField(
        upload_to="imagenes/", null=True, blank=True, default="channels4_profile.jpg")

    def __str__(self):
        return self.nombre

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.imagen.url))

    @property
    def get_photo_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return "/media/imagenes/default.png"

    class Meta:
        verbose_name = "proyectos"
        verbose_name_plural = "proyectos"

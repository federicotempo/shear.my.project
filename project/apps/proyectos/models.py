from django.db import models

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
        ProyectoCategoria, on_delete=models.DO_NOTHING, null=True, verbose_name="Categoría")
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")
    opciones = (('En proceso', 'En proceso'), ('Finalizado', 'Finalizado'))
    estado = models.CharField(max_length=100, choices=opciones)
    autor_id = models.ForeignKey(
        "autores.Autor", on_delete=models.DO_NOTHING, null=True, verbose_name="Autor")
    # colaboradores =
    # ubicacion =
    # imagen = models.ImageField(upload_to="imagenes", blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "proyectos"
        verbose_name_plural = "proyectos"

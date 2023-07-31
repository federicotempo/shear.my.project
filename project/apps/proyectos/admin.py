from django.contrib import admin
from .models import ProyectoCategoria, Proyecto

admin.site.site_title = "ProyectoCategoria"
admin.site.site_title = "Proyecto"


@admin.register(ProyectoCategoria)
class ProyectoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria_id",
                    "autor_id", "estado", "descripcion")
    list_filter = ("nombre", "categoria_id", "estado")
    search_fields = ("nombre", "categoria_id", "estado")
    ordering = ("nombre", "categoria_id", "estado")

from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "pais")
    list_filter = ("nombre", "apellido",)
    search_fields = ("nombre", "apellido", "email", "pais")
    ordering = ("nombre", "apellido", "pais")
    readonly_fields = ("admin_photo",)

from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    list_filter = ("nombre", "apellido",)
    search_fields = ("nombre", "apellido", "email")
    ordering = ("nombre", "apellido",)

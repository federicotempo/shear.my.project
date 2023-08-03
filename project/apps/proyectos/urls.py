from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

app_name = "proyectos"

urlpatterns = [
    path("proyectocategoria/list/", views.ProyectoCategoriaList.as_view(),
         name="proyectocategoria_list"),
    path("proyecto/list/", views.ProyectoList.as_view(),
         name="proyecto_list"),
    path("proyectocategoria/create/", views.ProyectoCategoriaCreate.as_view(),
         name="proyectocategoria_create"),
    path("proyecto/create/", views.ProyectoCreate.as_view(),
         name="proyecto_create"),
    path("proyectocategoria/delete/<int:pk>", views.ProyectoCategoriaDelete.as_view(),
         name="proyectocategoria_delete"),
    path("proyecto/delete/<int:pk>", views.ProyectoDelete.as_view(),
         name="proyecto_delete"),
    path("proyectos/index_categoria/",
         views.index_categoria, name="index_categoria"),
    path("proyectos/index_proyecto/",
         views.index_proyecto, name="index_proyecto"),
    path("proyecto/modificar/<id>/",
         views.modificar_proyecto, name="proyecto_modificar"),
    path("proyectocategoria/modificar/<id>/",
         views.modificar_proyectocategoria, name="proyectocategoria_modificar"),

]

urlpatterns += staticfiles_urlpatterns()

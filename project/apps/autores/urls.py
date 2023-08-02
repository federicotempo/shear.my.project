from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "autor"

urlpatterns = [
    path("autor/list/", views.AutorList.as_view(),
         name="autor_list"),
    path("autor/index/", views.index,
         name="index"),
    path("autor/create/", views.AutorCreate.as_view(),
         name="autor_create"),
    path("autor/delete/<int:pk>", views.AutorDelete.as_view(),
         name="autor_delete"),

]

urlpatterns += staticfiles_urlpatterns()

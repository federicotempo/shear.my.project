from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "autor"

urlpatterns = [
    path("autor/list/", views.AutorList.as_view(),
         name="autor_list"),

]

urlpatterns += staticfiles_urlpatterns()

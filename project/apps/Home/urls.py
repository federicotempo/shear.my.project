from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),

]

urlpatterns += staticfiles_urlpatterns()

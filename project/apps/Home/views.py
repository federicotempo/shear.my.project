from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from . import forms


def home(request):
    return render(request, "Home/index.html")


#!LOGIN

def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "Home/login.html", {"form": form})

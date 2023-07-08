from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
from .forms import LoginForm


# Create your views here.


def home(request):
    context ={}
    return render(request, "core/home.html")



def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core/perfil")
    else:
        form = LoginForm()
    return render(request, "core/inicio_sesion.html", {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, "core/register.html", {"form": form})


@login_required
def perfil(request):
        User = request.user
        return render(request, "core/perfil.html", {'User': User})
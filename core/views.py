import uuid
from django.shortcuts import get_object_or_404, redirect, render
from .models import User, Match, Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, MensajeForm, PerfilForm
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
                return redirect('perfil')
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


#@login_required
def perfil(request):
        User = request.user
        return render(request, "core/perfil.html", {'User': User})


#@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'form': form})
    
    
    
#@login_required    
def ver_perfil(request):
    usuario_actual = request.user
    User = User.objects.exclude(id=usuario_actual.id)
    match_id = None

    if request.method == 'POST':
        if 'like' in request.POST:
            usuario_id = int(request.POST.get('like'))
            usuario_destino = User.objects.get(id=usuario_id)
            match = Match(remite=usuario_actual, destino=usuario_destino)
            match.save()
            return redirect('chat', match_id=match.id)
        elif 'dislike' in request.POST:
            usuario_id = int(request.POST.get('dislike'))
            usuarios = usuarios.exclude(id=usuario_id)

    return render(request, 'perfiles.html', {'User': User, 'match_id': match_id})



#login_required   
def chat(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    mensajes = Mensaje.objects.filter(match=match).order_by('fecha')

    if request.method == 'POST':
        contenido = request.POST['contenido']
        id_mensaje = str(uuid.uuid4())[:10]  # Generar un ID único
        mensaje = Mensaje(remite=request.user, destino=match.destino, contenido=contenido, match=match, id_mensaje=id_mensaje)
        mensaje.save()

    return render(request, 'chat.html', {'match': match, 'mensajes': mensajes})
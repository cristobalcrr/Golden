from django.urls import path
from .views import home, register, iniciar_sesion, perfil, chat, editar_perfil


urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('inicio_sesion/', iniciar_sesion, name='inicio_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('chat/<int:match_id>/', chat, name='chat'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
]


 
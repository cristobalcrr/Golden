from django import forms
from .models import User, Mensaje
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'edad', 'numero_telefono', 'foto', 'descripcion')
        


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': True})
        

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destino', 'contenido']
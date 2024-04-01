from django.contrib.auth.forms import AuthenticationForm
from . import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={

            }
        )
    )
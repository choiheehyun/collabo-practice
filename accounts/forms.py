from django.contrib.auth.forms import AuthenticationForm, UsernameField, ReadOnlyPasswordHashField
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label= False,
        widget= forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )

    password = forms.CharField(
        label= False,
        widget = forms.PasswordInput(
            attrs={
                'class': 'input-box'
            }
        )
    )
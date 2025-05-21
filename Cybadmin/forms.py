from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Formulaire de connexion
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Formulaire d'enregistrement
class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'first name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'exemple@gmail.com'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'**************'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'**************'}),
        label="Confirm Password"
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


# Formulaire de changement de mot_de_passe
class ResetPassForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
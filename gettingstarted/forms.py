from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your full name"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your email"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message"
                    }
                )
            )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your username"}))
    email       = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "email"}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2    = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password2"}))

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

    def clean_username(self):
        username = self.clean_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
             raise form.ValidationError('username already exists')
        return username

    def clean_email(self):
        email = self.clean_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise form.ValidationError('email already registered')
        return email

    def clean_data(self):
        data = self.clean_data.get('data')
        password = self.clean_data.get('password')
        password2 = self.clean_data.get('password2')
        if password2 != password:
                raise form.ValidationError('passwords do not match')
        return data

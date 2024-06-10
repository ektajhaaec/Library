from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username=self.cleaned_data['username']
        if not username.isalnum():
            raise ValidationError('Username can only have alphanumeric character')
        return username
    def clean_password(self):
        password =self.cleaned_data['password']
        if len(password)<8:
            raise ValidationError('Password must be atleast 8 character long')
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain atleast one digit')
        if not any(char.isalpha() for char in password):
            raise ValidationError('Password must contain atleast one alphabet')
        return password
class LoginForm(forms.Form):
    username =forms.CharField(max_length =150)
    password= forms.CharField(widget=forms.PasswordInput)
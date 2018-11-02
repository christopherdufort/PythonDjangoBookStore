from django import forms
from .models import User


class AuthenticationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','password')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'password', 'phone_number', 'address')
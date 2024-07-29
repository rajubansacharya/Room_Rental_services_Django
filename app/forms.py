from django import forms
from django.forms import ModelForm
from app.models import list_room
from django.contrib.auth.forms import AuthenticationForm

class listForm(ModelForm):
    class Meta:
        model  = list_room
        fields = ["name" , "address" , "image"]

class loginForm(AuthenticationForm):
    # You can add custom fields or methods here if needed.
    # For example, adding a custom label to the username field:
    username = forms.CharField(label='Your Username')
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput)


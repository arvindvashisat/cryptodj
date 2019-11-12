from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, User
from . import forms
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','email','gender','mobile','phone','dob','address','city','state','country_id')
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'religious_order', 'nearest_town', 'county', 'year_founded', 'content', 'coordinates']

class PostSubmitForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
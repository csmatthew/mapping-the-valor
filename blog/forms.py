from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'religious_order', 'nearest_town', 'county', 'year_founded', 'content', 'coordinates']

class PostSubmitForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status']
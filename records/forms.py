from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, FinancialDetail
from django_summernote.widgets import SummernoteWidget
import re
import requests

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'county', 'year_founded', 'content', 'coordinates']
        widgets = {
            'name': forms.TextInput(attrs={'title': 'This field is required'}),
            'county': forms.TextInput(attrs={'title': 'This field is required'}),
            'year_founded': forms.NumberInput(attrs={'title': 'This field is required'}),
            'content': forms.Textarea(attrs={'title': 'This field is required'}),
            'coordinates': forms.TextInput(attrs={'title': 'This field is optional'}),
        }

    def clean_coordinates(self):
        coordinates = self.cleaned_data.get('coordinates')
        if not coordinates:
            return coordinates  # Return None if the field is empty

        dms_pattern = re.compile(r'([0-9.]+)°\s*([0-9.]+)′\s*([0-9.]+)″\s*([NS]),\s*([0-9.]+)°\s*([0-9.]+)′\s*([0-9.]+)″\s*([EW])')
        decimal_pattern = re.compile(r'([0-9.-]+),\s*([0-9.-]+)')
        original_pattern = re.compile(r'([0-9.]+)°([NS])\s*([0-9.]+)°([EW])')

        if not (dms_pattern.match(coordinates) or decimal_pattern.match(coordinates) or original_pattern.match(coordinates)):
            raise forms.ValidationError('Invalid coordinates format. Accepted formats: DMS (ex. 50° 39′ 52.1″ N, 2° 35′ 55.4″ W), Decimal (ex. 50.664472, -2.598722), or Original format.')

        return coordinates


class PostSubmitForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class FinancialDetailForm(forms.ModelForm):
    class Meta:
        model = FinancialDetail
        fields = ['holding_title', 'holding_pounds', 'holding_shillings', 'holding_pence']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Holding
from django_summernote.widgets import SummernoteWidget
import re
import requests

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'religious_order', 'nearest_town', 'county', 'year_founded', 'content', 'coordinates']
        widgets = {
            'name': forms.TextInput(attrs={'title': 'This field is required'}),
            'religious_order': forms.Select(attrs={'title': 'This field is required'}),
            'other_religious_order': forms.TextInput(attrs={'title': 'This field is optional'}),
            'nearest_town': forms.TextInput(attrs={'title': 'This field is required'}),
            'county': forms.TextInput(attrs={'title': 'This field is required'}),
            'year_founded': forms.NumberInput(attrs={'title': 'This field is required'}),
            'content': SummernoteWidget(),
            'coordinates': forms.TextInput(attrs={'title': 'This field is optional'}),
        }

    def clean_coordinates(self):
        coordinates = self.cleaned_data.get('coordinates')
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

class HoldingForm(forms.ModelForm):
    location_or_coordinates = forms.CharField(
        label='Location or Coordinates',
        help_text='Enter coordinates directly (latitude, longitude).'
    )

    class Meta:
        model = Holding
        fields = ['name', 'monastery', 'location_or_coordinates', 'value_pounds', 'value_shillings', 'value_pence']

    def clean_location_or_coordinates(self):
        input_value = self.cleaned_data['location_or_coordinates']
        dms_pattern = re.compile(r'([0-9.]+)°\s*([0-9.]+)′\s*([0-9.]+)″\s*([NS]),\s*([0-9.]+)°\s*([0-9.]+)′\s*([0-9.]+)″\s*([EW])')
        decimal_pattern = re.compile(r'([0-9.-]+),\s*([0-9.-]+)')
        original_pattern = re.compile(r'([0-9.]+)°([NS])\s*([0-9.]+)°([EW])')

        if not (dms_pattern.match(input_value) or decimal_pattern.match(input_value) or original_pattern.match(input_value)):
            raise forms.ValidationError('Invalid coordinates format. Accepted formats: DMS (ex. 50° 39′ 52.1″ N, 2° 35′ 55.4″ W), Decimal (ex. 50.664472, -2.598722), or Original format.')

        return input_value

    def save(self, commit=True):
        holding = super().save(commit=False)
        holding.coordinates = self.cleaned_data['location_or_coordinates']
        if commit:
            holding.save()
        return holding
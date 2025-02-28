from django import forms
from .models import ValorRecord, HouseType


class ValorRecordForm(forms.ModelForm):
    class Meta:
        model = ValorRecord
        fields = ['name', 'type', 'deanery']


class HouseTypeForm(forms.ModelForm):
    class Meta:
        model = HouseType
        fields = ['house_type']

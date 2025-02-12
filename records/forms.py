from django import forms
from .models.hierarchy import Diocese

class DioceseForm(forms.ModelForm):
    class Meta:
        model = Diocese
        fields = ['name', 'province']

    def clean_province(self):
        province = self.cleaned_data.get('province')
        if not province:
            raise forms.ValidationError("You must select a province.")
        return province
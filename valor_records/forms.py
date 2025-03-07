from django import forms
from .models import ValorRecord, HouseType


class ValorRecordForm(forms.ModelForm):
    house_type = forms.ModelChoiceField(
        queryset=HouseType.objects.all(),
        required=False,
        label='House Type'
    )

    class Meta:
        model = ValorRecord
        fields = [
            'name', 'record_type', 'deanery',
            'latitude', 'longitude', 'house_type'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.house_type:
            self.fields['house_type'].initial = self.instance.house_type

    def save(self, commit=True):
        instance = super().save(commit=False)
        house_type = self.cleaned_data.get('house_type')

        if house_type and instance.record_type == 'Monastery':
            instance.house_type = house_type
        else:
            instance.house_type = None

        if commit:
            instance.save()

        return instance

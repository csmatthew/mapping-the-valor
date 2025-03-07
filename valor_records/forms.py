from django import forms
from .models import ValorRecord, HouseType


class ValorRecordForm(forms.ModelForm):
    house_type = forms.ChoiceField(
        choices=HouseType.HOUSE_TYPE_CHOICES,
        required=False,
        label='House Type'
    )

    class Meta:
        model = ValorRecord
        fields = ['name', 'record_type', 'deanery', 'house_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and hasattr(self.instance, 'housetype'):
            self.fields['house_type'].initial = (
                self.instance.housetype.house_type
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        house_type = self.cleaned_data.get('house_type')

        if commit:
            instance.save()
            if house_type:
                HouseType.objects.update_or_create(
                    valor_record=instance,
                    defaults={'house_type': house_type}
                )
            else:
                HouseType.objects.filter(valor_record=instance).delete()

        return instance


class HouseTypeForm(forms.ModelForm):
    class Meta:
        model = HouseType
        fields = ['house_type']

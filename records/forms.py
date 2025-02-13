from django import forms
from dal import autocomplete
from .models.hierarchy import Diocese, Archdeaconry, Deanery, Parish
from .models.valor_record import ValorRecord


class DioceseForm(forms.ModelForm):
    class Meta:
        model = Diocese
        fields = ['name', 'province']

    def clean_province(self):
        province = self.cleaned_data.get('province')
        if not province:
            raise forms.ValidationError("You must select a province.")
        return province


class ArchdeaconryForm(forms.ModelForm):
    class Meta:
        model = Archdeaconry
        fields = ['name', 'diocese']
        widgets = {
            'diocese': autocomplete.ModelSelect2(url='diocese-autocomplete')
        }

    def clean_diocese(self):
        diocese = self.cleaned_data.get('diocese')
        if not diocese:
            raise forms.ValidationError("You must select a valid diocese.")
        return diocese


class DeaneryForm(forms.ModelForm):
    class Meta:
        model = Deanery
        fields = ['name', 'archdeaconry']
        widgets = {
            'archdeaconry': autocomplete.ModelSelect2(
                url='archdeaconry-autocomplete'
            )
        }

    def clean_archdeaconry(self):
        archdeaconry = self.cleaned_data.get('archdeaconry')
        if not archdeaconry:
            raise forms.ValidationError(
                "You must select a valid archdeaconry."
            )
        return archdeaconry


class ParishForm(forms.ModelForm):
    class Meta:
        model = Parish
        fields = ['name', 'deanery']
        widgets = {
            'deanery': autocomplete.ModelSelect2(
                url='deanery-autocomplete'
            )
        }

    def clean_deanery(self):
        deanery = self.cleaned_data.get('deanery')
        if not deanery:
            raise forms.ValidationError(
                "You must select a valid deanery."
            )
        return deanery


class ValorRecordForm(forms.ModelForm):
    class Meta:
        model = ValorRecord
        fields = [
            'name', 'content', 'slug', 'record_type', 'province',
            'diocese', 'archdeaconry', 'deanery', 'parish'
        ]
        widgets = {
            'province': autocomplete.ModelSelect2(
                url='province-autocomplete'
            ),
            'diocese': autocomplete.ModelSelect2(
                url='diocese-autocomplete', forward=['province']
            ),
            'archdeaconry': autocomplete.ModelSelect2(
                url='archdeaconry-autocomplete', forward=['diocese']
            ),
            'deanery': autocomplete.ModelSelect2(
                url='deanery-autocomplete', forward=['archdeaconry']
            ),
            'parish': autocomplete.ModelSelect2(
                url='parish-autocomplete', forward=['deanery']
            ),
        }

from django.contrib import admin
from dal import autocomplete
from .models.valor_record import ValorRecord
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish
from .forms import (
    DioceseForm, ArchdeaconryForm, DeaneryForm, ParishForm, ValorRecordForm
)


class ValorRecordAdmin(admin.ModelAdmin):
    form = ValorRecordForm
    list_display = (
        'name', 'record_type', 'province', 'diocese',
        'archdeaconry', 'deanery', 'parish', 'created_at', 'updated_at'
    )
    list_filter = (
        'record_type', 'province', 'diocese',
        'archdeaconry', 'deanery', 'parish'
    )
    search_fields = ('name', 'content')

    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.js',
            'admin/js/jquery.init.js',
            'admin/js/actions.js'
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'diocese':
            kwargs['widget'] = autocomplete.ModelSelect2(
                url='diocese-autocomplete',
                forward=['province']
            )
        elif db_field.name == 'archdeaconry':
            kwargs['widget'] = autocomplete.ModelSelect2(
                url='archdeaconry-autocomplete',
                forward=['diocese']
            )
        elif db_field.name == 'deanery':
            kwargs['widget'] = autocomplete.ModelSelect2(
                url='deanery-autocomplete',
                forward=['archdeaconry']
            )
        elif db_field.name == 'parish':
            kwargs['widget'] = autocomplete.ModelSelect2(
                url='parish-autocomplete',
                forward=['deanery']
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DioceseAdmin(admin.ModelAdmin):
    form = DioceseForm
    list_display = ('name', 'province')
    search_fields = ('name', 'province__name')


class ArchdeaconryAdmin(admin.ModelAdmin):
    form = ArchdeaconryForm
    list_display = ('name', 'diocese')
    search_fields = ('name', 'diocese__name')


class DeaneryAdmin(admin.ModelAdmin):
    form = DeaneryForm
    list_display = ('name', 'archdeaconry')
    search_fields = ('name', 'archdeaconry__name')


class ParishAdmin(admin.ModelAdmin):
    form = ParishForm
    list_display = ('name', 'deanery')
    search_fields = ('name', 'deanery__name')


admin.site.register(Province)
admin.site.register(Diocese, DioceseAdmin)
admin.site.register(Archdeaconry, ArchdeaconryAdmin)
admin.site.register(Deanery, DeaneryAdmin)
admin.site.register(Parish, ParishAdmin)
admin.site.register(ValorRecord, ValorRecordAdmin)

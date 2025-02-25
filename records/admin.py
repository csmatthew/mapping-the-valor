from django.contrib import admin
from dal import autocomplete
from .models.valor_record import ValorRecord
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish
from .models.holding import Holding
from .models.monastery import Monastery
from .forms import (
    DioceseForm, ArchdeaconryForm, DeaneryForm,
    ParishForm, ValorRecordForm, MonasteryForm
)


class HoldingInline(admin.TabularInline):
    model = Holding
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        return 1

    def get_verbose_name(self, obj):
        return f"Holdings for {obj.name}"


class ValorRecordAdmin(admin.ModelAdmin):
    form = ValorRecordForm
    list_display = (
        'name', 'record_type', 'province', 'diocese',
        'archdeaconry', 'deanery', 'monastery',
        'created_at', 'updated_at'
    )
    list_filter = (
        'record_type', 'province', 'diocese', 'archdeaconry',
        'deanery', 'monastery'
    )
    search_fields = ('name', 'content')
    inlines = [HoldingInline]

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
        elif db_field.name == 'monastery':
            kwargs['widget'] = autocomplete.ModelSelect2(
                url='monastery-autocomplete'
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


class MonasteryAdmin(admin.ModelAdmin):
    form = MonasteryForm
    list_display = (
        'monastery_name',
        'house_type',
        'religious_order',
        'abbot',
        'latitude',
        'longitude',
        'source',
    )
    search_fields = ('monastery_name', 'abbot')
    fields = (
        'monastery_name',
        'house_type',
        'religious_order',
        'abbot',
        'latitude',
        'longitude',
        'source',
    )


admin.site.register(Province)
admin.site.register(Diocese, DioceseAdmin)
admin.site.register(Archdeaconry, ArchdeaconryAdmin)
admin.site.register(Deanery, DeaneryAdmin)
admin.site.register(Parish, ParishAdmin)
admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(Monastery, MonasteryAdmin)

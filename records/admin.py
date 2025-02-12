from django.contrib import admin
from dal import autocomplete
from .models.valor_record import ValorRecord
from .models.hierarchy import Province, Diocese

class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'record_type', 'province', 'diocese', 'archdeaconry', 'deanery', 'created_at', 'updated_at')
    list_filter = ('record_type', 'province', 'diocese', 'archdeaconry', 'deanery')
    search_fields = ('name', 'content')

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/jquery.init.js', 'admin/js/actions.js')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'diocese':
            kwargs['widget'] = autocomplete.ModelSelect2(url='diocese-autocomplete', forward=['province'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Province)
admin.site.register(Diocese)
admin.site.register(ValorRecord, ValorRecordAdmin)

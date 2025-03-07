from django.contrib import admin
from .models import ValorRecord, Deanery
from .forms import ValorRecordForm


class DeaneryAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False  # Hides Deanery from the admin sidebar


class ValorRecordAdmin(admin.ModelAdmin):
    form = ValorRecordForm
    list_display = (
        'name', 'record_type', 'deanery', 'created_by',
        'last_edited_by', 'get_house_type', 'date_created', 'date_updated'
    )
    list_filter = ('record_type', 'deanery')
    search_fields = ('name',)

    class Media:
        js = ('admin/js/valor_record.js',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the record is being created
            obj.created_by = request.user
        obj.last_edited_by = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'created_by' in form.base_fields:
            del form.base_fields['created_by']
        if 'last_edited_by' in form.base_fields:
            del form.base_fields['last_edited_by']
        return form

    def get_house_type(self, obj):
        return obj.house_type.house_type if obj.house_type else None
    get_house_type.short_description = 'House Type'


# Register the models with the custom admin
admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(Deanery, DeaneryAdmin)

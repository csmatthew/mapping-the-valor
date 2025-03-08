from django.contrib import admin
from .models import ValorRecord
from .forms import ValorRecordForm


class ValorRecordAdmin(admin.ModelAdmin):
    form = ValorRecordForm
    list_display = (
        'name', 'record_type', 'deanery', 'created_by',
        'last_edited_by', 'get_house_type', 'get_religious_order',
        'date_created', 'date_updated'
    )
    list_filter = ('record_type', 'deanery', 'religious_order')
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
        return str(obj.house_type) if obj.house_type else None
    get_house_type.short_description = 'House Type'

    def get_religious_order(self, obj):
        return str(obj.religious_order) if obj.religious_order else None
    get_religious_order.short_description = 'Religious Order'


# Register the models with the custom admin
admin.site.register(ValorRecord, ValorRecordAdmin)

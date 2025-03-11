from django.contrib import admin
from django.contrib import messages
from .models import ValorRecord
from .forms import ValorRecordForm


class ValorRecordAdmin(admin.ModelAdmin):
    form = ValorRecordForm
    list_display = (
        'name', 'slug', 'record_type', 'deanery',
        'status', 'last_edited_by', 'get_house_type', 'get_religious_order',
        'source_ref_vol', 'source_ref_page'
    )
    list_filter = ('record_type', 'deanery', 'religious_order', 'status')
    search_fields = ('name',)
    actions = ['approve_records']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'record_type', 'deanery', 'status', 'house_type', 'religious_order', 'latitude', 'longitude', 'source_ref_vol', 'source_ref_page')
        }),
        ('User Information', {
            'fields': ('created_by', 'last_edited_by'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('slug', 'created_by', 'last_edited_by')

    class Media:
        js = ('admin/js/valor_record.js',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the record is being created
            obj.created_by = request.user
        obj.last_edited_by = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        kwargs['user'] = request.user
        form = super().get_form(request, obj, **kwargs)
        if 'created_by' in form.base_fields:
            del form.base_fields['created_by']
        if 'last_edited_by' in form.base_fields:
            del form.base_fields['last_edited_by']
        if not request.user.is_superuser:
            form.base_fields['status'].disabled = True
        return form

    def get_house_type(self, obj):
        return str(obj.house_type) if obj.house_type else None
    get_house_type.short_description = 'House Type'

    def get_religious_order(self, obj):
        return str(obj.religious_order) if obj.religious_order else None
    get_religious_order.short_description = 'Religious Order'

    def approve_records(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} record(s) successfully approved.", messages.SUCCESS)
    approve_records.short_description = "Approve selected records"


admin.site.register(ValorRecord, ValorRecordAdmin)

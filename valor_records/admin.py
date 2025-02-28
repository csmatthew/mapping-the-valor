from django.contrib import admin
from .models import ValorRecord, HouseType, Deanery


class HouseTypeInline(admin.StackedInline):
    model = HouseType
    can_delete = False
    verbose_name_plural = 'House Type'


class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'record_type', 'deanery', 'created_by', 'last_edited_by', 'date_created', 'date_updated')
    list_filter = ('record_type', 'deanery')
    search_fields = ('name',)

    inlines = [HouseTypeInline]

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        """
        Ensure that the form does not include created_by and last_edited_by as fields in the ValorRecord form.
        """
        form = super().get_form(request, obj, **kwargs)
        if 'created_by' in form.base_fields:
            del form.base_fields['created_by']
        if 'last_edited_by' in form.base_fields:
            del form.base_fields['last_edited_by']
        return form


# Register the models with the custom admin
admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(Deanery)  # Register Deanery separately

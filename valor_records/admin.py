from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import ValorRecord, HouseType, Deanery


class HouseTypeInline(admin.StackedInline):
    model = HouseType
    can_delete = False
    verbose_name_plural = 'House Type'
    extra = 0
    max_num = 1


class DeaneryAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False  # Hides Deanery from the admin sidebar


class ValorRecordAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'record_type', 'deanery', 'created_by',
        'last_edited_by', 'get_house_type', 'date_created', 'date_updated'
    )
    list_filter = ('record_type', 'deanery')
    search_fields = ('name',)
    inlines = [HouseTypeInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the record is being created
            obj.created_by = request.user
        obj.last_edited_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, HouseType):
                if (form.instance.record_type == ValorRecord.MONASTERY and
                        not instance.house_type):
                    raise ValidationError(
                        'A Monastery must have an associated House type.'
                    )
            instance.save()
        formset.save_m2m()

    def get_form(self, request, obj=None, **kwargs):
        """
        Ensure that the form does not include created_by and last_edited_by
        as fields in the ValorRecord form.
        """
        form = super().get_form(request, obj, **kwargs)
        if 'created_by' in form.base_fields:
            del form.base_fields['created_by']
        if 'last_edited_by' in form.base_fields:
            del form.base_fields['last_edited_by']
        return form

    def get_house_type(self, obj):
        return obj.housetype.house_type if hasattr(obj, 'housetype') else None
    get_house_type.short_description = 'House Type'


# Register the models with the custom admin
admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(Deanery, DeaneryAdmin)

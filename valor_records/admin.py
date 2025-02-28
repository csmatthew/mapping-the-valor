from django.contrib import admin
from .models import ValorRecord, HouseType


class HouseTypeInline(admin.StackedInline):
    model = HouseType
    can_delete = False
    verbose_name_plural = 'House Type'


class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'deanery')
    list_filter = ('type', 'deanery')
    search_fields = ('name',)

    # Add HouseType inline form only if the ValorRecord is a Monastery
    inlines = [HouseTypeInline]


# Register the models
admin.site.register(ValorRecord, ValorRecordAdmin)

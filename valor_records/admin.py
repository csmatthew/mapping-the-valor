from django.contrib import admin
from .models import Deanery, Institution, HouseType

# Register your models here.


@admin.register(Deanery)
class DeaneryAdmin(admin.ModelAdmin):
    list_display = ('deanery_name',)
    search_fields = ('deanery_name',)


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'deanery')
    search_fields = ('name', 'type', 'deanery__deanery_name')
    list_filter = ('type', 'deanery')


@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('institution', 'house_type')
    search_fields = ('institution__name', 'house_type')
    list_filter = ('house_type',)

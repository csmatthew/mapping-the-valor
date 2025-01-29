from django.contrib import admin
from .models import ValorRecord
from django_summernote.admin import SummernoteModelAdmin

class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on', 'updated_on')
    search_fields = ('name', 'content')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_on'
    ordering = ('status', 'created_on')

admin.site.register(ValorRecord, ValorRecordAdmin)
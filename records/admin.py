from django.contrib import admin
from .models import ValorRecord, County, ReligiousOrder, Monastery

# Create Inline Admin for related models if needed (use only if you need inline editing)
class CountyInline(admin.TabularInline):
    model = ValorRecord
    fields = ('county',)  # Display only the 'county' field
    extra = 1

class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'county', 'status', 'created_on', 'updated_on')
    list_filter = ('county', 'status')
    search_fields = ('name', 'author__username', 'county__name')

    # No need to include inlines for ForeignKeys directly
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'author', 'content', 'status')
        }),
        ('Location Information', {
            'fields': ('county',),
            'classes': ('collapse',),  # Makes this section collapsible
        }),
    )

admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(County)
admin.site.register(ReligiousOrder)
admin.site.register(Monastery)

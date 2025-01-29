from django.contrib import admin
from .models import ValorRecord, County, ReligiousOrder, Monastery, HouseType

class MonasteryInline(admin.StackedInline):
    model = Monastery
    extra = 0
    max_num = 1

class ValorRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'county', 'type', 'status', 'created_on', 'updated_on')
    list_filter = ('county', 'type', 'status')
    search_fields = ('name', 'author__username', 'county__name')

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'author', 'content', 'status', 'type')
        }),
        ('Location Information', {
            'fields': ('county',),
            'classes': ('collapse',),  # Makes this section collapsible
        }),
        ('Dates', {
            'fields': ('construction_date', 'created_on', 'updated_on'),
        }),
    )

    readonly_fields = ('created_on', 'updated_on')

    inlines = [MonasteryInline]

    class Media:
        js = ('js/admin.js',)

admin.site.register(ValorRecord, ValorRecordAdmin)
admin.site.register(County)
admin.site.register(ReligiousOrder)
admin.site.register(HouseType)
admin.site.register(Monastery)

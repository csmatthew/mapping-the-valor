from django.contrib import admin
from .models import Post, HouseType, FinancialDetail
from django_summernote.admin import SummernoteModelAdmin

class FinancialDetailInline(admin.TabularInline):
    model = FinancialDetail
    extra = 1  # Number of empty forms to display

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status=2)

class PostAdmin(SummernoteModelAdmin):  # Use SummernoteModelAdmin
    list_display = ('name', 'county', 'status', 'year_founded', 'created_by', 'created_on')
    actions = [make_published]
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)  # Specify the fields to use Summernote
    inlines = [FinancialDetailInline]  # Add the inline form

admin.site.register(Post, PostAdmin)
admin.site.register(HouseType)
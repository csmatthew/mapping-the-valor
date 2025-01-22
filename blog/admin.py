from django.contrib import admin
from .models import Post, ReligiousOrder
from django_summernote.admin import SummernoteModelAdmin

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status=2)

class PostAdmin(SummernoteModelAdmin):  # Use SummernoteModelAdmin
    list_display = ('name', 'status', 'created_by', 'created_on')
    actions = [make_published]
    summernote_fields = ('content',)  # Specify the fields to use Summernote

admin.site.register(Post, PostAdmin)
admin.site.register(ReligiousOrder)
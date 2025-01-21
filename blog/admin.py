from django.contrib import admin
from .models import Post, ReligiousOrder

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status=2)

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by', 'created_on')
    actions = [make_published]

admin.site.register(Post, PostAdmin)
admin.site.register(ReligiousOrder)
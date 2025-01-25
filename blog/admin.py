from django.contrib import admin
from .models import Post, ReligiousOrder, HouseType, Holding
from .forms import HoldingForm
from django_summernote.admin import SummernoteModelAdmin

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status=2)

class PostAdmin(SummernoteModelAdmin):  # Use SummernoteModelAdmin
    list_display = ('name', 'status', 'created_by', 'created_on')
    actions = [make_published]
    summernote_fields = ('content',)  # Specify the fields to use Summernote

class HoldingAdmin(admin.ModelAdmin):
    form = HoldingForm
    list_display = ('name', 'monastery', 'location_or_coordinates', 'value_pounds', 'value_shillings', 'value_pence')

    def location_or_coordinates(self, obj):
        return obj.coordinates

    def save_model(self, request, obj, form, change):
        if not obj.monastery_id:
            obj.monastery = form.cleaned_data.get('monastery')
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(ReligiousOrder)
admin.site.register(HouseType)
admin.site.register(Holding, HoldingAdmin)
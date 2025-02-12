from dal import autocomplete
from .models.hierarchy import Diocese


class DioceseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Diocese.objects.none()

        qs = Diocese.objects.all()

        province_id = self.forwarded.get('province', None)

        if province_id:
            qs = qs.filter(province_id=province_id)

        return qs

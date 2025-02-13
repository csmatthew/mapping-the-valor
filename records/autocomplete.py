from dal import autocomplete
from .models.hierarchy import Diocese, Archdeaconry


class DioceseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Diocese.objects.none()

        qs = Diocese.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class ArchdeaconryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Archdeaconry.objects.none()

        qs = Archdeaconry.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

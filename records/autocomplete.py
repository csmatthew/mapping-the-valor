from dal import autocomplete
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish


class ProvinceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Province.objects.none()

        qs = Province.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class DioceseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Diocese.objects.none()

        qs = Diocese.objects.all().order_by('name')

        province = self.forwarded.get('province', None)
        if province:
            qs = qs.filter(province_id=province)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class ArchdeaconryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Archdeaconry.objects.none()

        qs = Archdeaconry.objects.all().order_by('name')

        diocese = self.forwarded.get('diocese', None)
        if diocese:
            qs = qs.filter(diocese_id=diocese)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class DeaneryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Deanery.objects.none()

        qs = Deanery.objects.all().order_by('name')

        archdeaconry = self.forwarded.get('archdeaconry', None)
        if archdeaconry:
            qs = qs.filter(archdeaconry_id=archdeaconry)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class ParishAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Parish.objects.none()

        qs = Parish.objects.all().order_by('name')

        deanery = self.forwarded.get('deanery', None)
        if deanery:
            qs = qs.filter(deanery_id=deanery)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

from django.urls import path
from .autocomplete import (
    ProvinceAutocomplete,
    DioceseAutocomplete,
    ArchdeaconryAutocomplete,
    DeaneryAutocomplete,
    ParishAutocomplete
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'province-autocomplete/',
        ProvinceAutocomplete.as_view(),
        name='province-autocomplete'
    ),
    path(
        'diocese-autocomplete/',
        DioceseAutocomplete.as_view(),
        name='diocese-autocomplete'
    ),
    path(
        'archdeaconry-autocomplete/',
        ArchdeaconryAutocomplete.as_view(),
        name='archdeaconry-autocomplete'
    ),
    path(
        'deanery-autocomplete/',
        DeaneryAutocomplete.as_view(),
        name='deanery-autocomplete'
    ),
    path(
        'parish-autocomplete/',
        ParishAutocomplete.as_view(),
        name='parish-autocomplete'
    ),
]

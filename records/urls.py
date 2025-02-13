from django.urls import path
from .autocomplete import DioceseAutocomplete, ArchdeaconryAutocomplete
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
]

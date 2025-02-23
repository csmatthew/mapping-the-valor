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
    path('create-post/', views.create_post, name='create_post'),
    path('search/', views.search, name='search'),
    path(
        'archdeaconry/<int:pk>/',
        views.archdeaconry_detail,
        name='archdeaconry_detail'
    ),
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

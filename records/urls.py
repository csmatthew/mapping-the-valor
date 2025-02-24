from django.urls import path
from .autocomplete import (
    ProvinceAutocomplete,
    DioceseAutocomplete,
    ArchdeaconryAutocomplete,
    DeaneryAutocomplete,
    ParishAutocomplete
)
from . import views
from .models.hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish

urlpatterns = [
    path('', views.index, name='index'),
    path('create-post/', views.create_post, name='create_post'),
    path('explore/', views.explore, name='explore'),
    path(
        'explore/provinces/',
        views.explore_provinces, name='explore_provinces'
    ),
    path(
        'explore/dioceses/',
        views.explore_dioceses, name='explore_dioceses'
    ),
    path(
        'explore/archdeaconries/',
        views.explore_archdeaconries, name='explore_archdeaconries'
    ),
    path(
        'explore/deaneries/',
        views.explore_deaneries, name='explore_deaneries'
    ),
    path(
        'explore/parishes/',
        views.explore_parishes, name='explore_parishes'
    ),
    path(
        'province/<int:pk>/',
        views.HierarchyDetailView.as_view(model=Province),
        name='province_detail'
    ),
    path(
        'diocese/<int:pk>/',
        views.HierarchyDetailView.as_view(model=Diocese),
        name='diocese_detail'
    ),
    path(
        'archdeaconry/<int:pk>/',
        views.HierarchyDetailView.as_view(model=Archdeaconry),
        name='archdeaconry_detail'
    ),
    path(
        'deanery/<int:pk>/',
        views.HierarchyDetailView.as_view(model=Deanery),
        name='deanery_detail'
    ),
    path(
        'parish/<int:pk>/',
        views.HierarchyDetailView.as_view(model=Parish),
        name='parish_detail'
    ),
    path(
        'valorrecord/<int:pk>/',
        views.ValorRecordDetailView.as_view(),
        name='valorrecord_detail'
    ),
    path(
        'monastery/<int:pk>/',
        views.MonasteryDetailView.as_view(),
        name='monastery_detail'
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

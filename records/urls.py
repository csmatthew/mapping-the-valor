from django.urls import path
from .autocomplete import DioceseAutocomplete
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'diocese-autocomplete/',
        DioceseAutocomplete.as_view(),
        name='diocese-autocomplete'
    ),
]

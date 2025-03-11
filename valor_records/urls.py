from django.urls import path
from .views import (
    valor_record_detail,
    ValorRecordCreateView,
    ValorRecordUpdateView,
    ValorRecordDeleteView,
)

urlpatterns = [
    path(
        '<slug:slug>/',
        valor_record_detail,
        name='valor_record_detail'
    ),
    path(
        'create/',
        ValorRecordCreateView.as_view(),
        name='valor_record_create'
    ),
    path(
        '<slug:slug>/update/',
        ValorRecordUpdateView.as_view(),
        name='valor_record_update'
    ),
    path(
        '<slug:slug>/delete/',
        ValorRecordDeleteView.as_view(),
        name='valor_record_delete'
    ),
]

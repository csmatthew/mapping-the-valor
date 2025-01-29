from django.urls import path
from .views import index, ValorRecordListView

urlpatterns = [
    path('', index, name='index'),
    path('valor-records/', ValorRecordListView.as_view(), name='valor_list'),
]
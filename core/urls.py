from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('valor-record/', include('valor_records.urls')),
]

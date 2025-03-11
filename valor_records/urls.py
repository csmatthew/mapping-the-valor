from django.urls import path
from .views import valor_record_detail


urlpatterns = [
    path('<slug:slug>/', valor_record_detail, name='valor_record_detail'),
]

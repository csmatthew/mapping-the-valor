from django.urls import path
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),  # Home page URL
    path('map/', views.monasteries_map, name='monasteries_map'),  # Map page URL
]
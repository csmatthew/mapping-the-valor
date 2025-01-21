from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.monasteries_map, name='monasteries_map'),
    path('', views.monasteries_map, name='home'),  # Add this line to handle the root path
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('create/', views.create_post, name='create_post'),
]
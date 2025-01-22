from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('drafts/', views.view_drafts, name='view_drafts'),  # Add URL pattern for viewing drafts
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('drafts/', views.view_drafts, name='view_drafts'),
    path('post/<int:pk>/edit/', views.update_post, name='update_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
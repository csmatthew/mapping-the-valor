from django.urls import path
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('drafts/', views.view_drafts, name='view_drafts'),
    path('post/<slug:slug>/edit/', views.update_post, name='update_post'),
    path('post/<int:pk>/submit/', views.submit_for_approval, name='submit_for_approval'),
    path('post/<int:pk>/approve/', views.approve_post, name='approve_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('monastery/<int:monastery_id>/add_holding/', views.add_holding, name='add_holding'), 
]
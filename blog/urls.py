from django.urls import path
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('post/<int:pk>/submit/', views.submit_for_approval, name='submit_for_approval'),
    path('post/<int:pk>/approve/', views.approve_post, name='approve_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.monasteries_map, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='account_logout'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('submit-for-approval/<int:pk>/', views.submit_for_approval, name='submit_for_approval'),
    path('approve-post/<int:pk>/', views.approve_post, name='approve_post'),
    path('accounts/', include('allauth.urls')),
    path('update-financial-detail/', views.update_financial_detail, name='update_financial_detail'),
    path('delete-financial-detail/', views.delete_financial_detail, name='delete_financial_detail'),
]
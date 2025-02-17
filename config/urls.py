from django.contrib import admin
from django.urls import path, include
from records import views as records_views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', records_views.index, name='home'),
]

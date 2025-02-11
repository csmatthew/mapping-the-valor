from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('summernote/', include('django_summernote.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]
from django.contrib import admin
from django.urls import path, include
from mapper.views import map_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_view, name='home'),
    path('core/', include('core.urls')),
    path('map/', include('mapper.urls')),
    path('valor-records/', include('valor_records.urls')),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
]

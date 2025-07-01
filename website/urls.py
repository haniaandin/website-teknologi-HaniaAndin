from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artikel.urls')),  # Landing page diarahkan ke app artikel
    path('', views.index, name='galeri_index'),  # Galeri (kalau punya halaman tersendiri)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
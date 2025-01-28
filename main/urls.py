from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('library.urls')),
    path('hashtags/', include('hashtags.urls')),
    path('basket/', include('basket.urls')),
    path('library_parsing/', include('library_parsing.urls')),
    path('employee_finder/', include('employee_finder.urls')),
    path('recipes/', include('recipes.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
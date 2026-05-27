"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visa.urls')),  # Include visa app URLs
]

# Serve media files in development and testing
# Note: WhiteNoise serves static files automatically in production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Error handlers for development
    urlpatterns += [
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not found")}),
        path('500/', default_views.server_error),
    ]
else:
    # In production (DEBUG=False), also serve media files
    # Static files are handled by WhiteNoise middleware
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler404 = 'visa.views.error_404'
handler500 = 'visa.views.error_500'

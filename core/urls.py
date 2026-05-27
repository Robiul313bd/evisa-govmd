"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from visa.views import error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visa.urls')),  # Include visa app URLs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Error handlers for development
    urlpatterns += [
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not found")}),
        path('500/', default_views.server_error),
    ]

# Catch-all pattern for 404 errors (must be last)
urlpatterns += [
    re_path(r'^.*$', error_404, name='catch_all_404'),
]

# Error handlers
handler404 = 'visa.views.error_404'
handler500 = 'visa.views.error_500'

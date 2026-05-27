"""
URL patterns for visa app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-my-visa/', views.check_visa, name='check_visa'),
    path('download-pdf/<int:visa_id>/', views.download_visa_pdf, name='download_visa_pdf'),
]

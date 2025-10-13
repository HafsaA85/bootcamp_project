"""
URL configuration for bootcamp_project project.
"""

from django.contrib import admin
from django.urls import path, include
from clients import views as client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client_views.home, name='home'),         
    path('clients/', include('clients.urls')),         
]

"""
URL configuration for Geodata_processing_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from geo_base import views


urlpatterns = [
    path('', views.main_page, name='welcome'),
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
    path('geo_base/', include('geo_base.urls')),
    # path('position/', views.position_page, name='position_page'),
    # path('data_transfer/', views.data_transfer, name='data_transfer_page'),
]

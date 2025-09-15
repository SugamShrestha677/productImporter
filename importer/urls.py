"""
URL configuration for importer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# importer/urls.py
# importer/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products import views # Import views from your products app

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL for your file upload page
    path('', include('products.urls')),
    
    # URLs for your DRF API
    path('api/', include(router.urls)),
]
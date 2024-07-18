from django.contrib import admin
from django.urls import path, include
from warehouse.admin_site import admin_site  

urlpatterns = [
    path('admin/', admin_site.urls),
     path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
    path('', include('warehouse.urls')),
]

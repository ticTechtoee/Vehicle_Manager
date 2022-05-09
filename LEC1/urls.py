from django.contrib import admin
from django.urls import path, include
import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('save/', include('add_vehicle.urls')),
    #path('owner/', include('add_owner.urls')),
    
]

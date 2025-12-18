
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('houses/', include('houses.urls')),
    path('jobs/', include('jobs.urls')),
    path('services/', include('services.urls')),
    path('biznis/', include('biznis.urls')),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('authentication.urls')),
    path('', include('doctors.urls')),
    path('', include('patients.urls')),
    path('', include('inventory.urls'))
]

from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/patients/', views.patientsDashboard, name='patients_dashboard')
]

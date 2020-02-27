from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard')
    # path('dashboard/patients/', views.patientsDashboard, name='patients_dashboard'),
    # path('dashboard/analytics/', views.analyticsDasboard, name='analytics_dashboard'),
]

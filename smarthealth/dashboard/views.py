from django.shortcuts import render

def patientsDashboard(request):

    return render(request, 'dashboards/views/patient_dashboard.html', {})

def analyticsDasboard(request):

    pass
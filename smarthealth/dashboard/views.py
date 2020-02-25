from django.shortcuts import render
from patients.models import Patient

def patientsDashboard(request):

    patient = Patient.objects.all()

    total_patients = patient.count()

    context = {
        'total_patients' : total_patients
    }

    return render(request, 'dashboards/views/patient_dashboard.html', context)


def analyticsDasboard(request):

    return render(request, 'dashboards/views/analytics_dashboard.html', {})
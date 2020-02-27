from datetime import date, datetime
from time import strftime

from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncDate
from django.shortcuts import render, redirect
# from pipenv.vendor.tomlkit import item

from users.models import CustomUser


def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST:
                if request.user.is_superuser:
                    hashed = make_password(request.POST['password2'])
                    obj = CustomUser.objects.create(username=request.POST['username'],
                                                    email=request.POST['email'],
                                                    password=hashed,
                                                    userType=request.POST['userType'],
                                                    hospitalName=request.POST['hospitalName']
                                                    )
                    obj.save()
                    if request.user.is_authenticated:
                        return redirect('dashboard')
                    else:
                        return render(request, 'authentication/views/error.html', {})
                elif request.user.userType == 'Client':
                    hashed = make_password(request.POST['password2'])
                    obj = CustomUser.objects.create(
                        username=request.POST['username'],
                        firstName=request.POST['firstName'],
                        middleName=request.POST['middleName'],
                        lastName=request.POST['lastName'],
                        gender=request.POST['gender'],
                        specialization=request.POST['specialization'],
                        email=request.POST['email'],
                        mobile_number=request.POST['mobile_number'],
                        homeAddress=request.POST['homeAddress'],
                        password=hashed
                    )
                    obj.save()
                    if request.user.is_authenticated:
                        return redirect('dashboard')
                    else:
                        return render(request, 'authentication/views/error.html', {})
        return render(request, 'dashboards/views/patient_dashboard.html', {})
    else:
        return redirect('users:login')
def analytic_dashbaord(request):
    if request.user.userType == 'Doctor' or request.user.userType == 'Client':
        return render(request, 'dashboards/views/analytics_dashboard.html', {})
    else:
        return render(request, 'authentication/views/error.html', {})

def client_dashboard(request):
    if request.user.is_superuser:
        today = date.today().strftime('%m')
        print(today)
        qs = CustomUser.objects.filter(userType='Client').count()
        sample = CustomUser.objects.annotate(month=TruncMonth('date_joined'))\
            .values('month').annotate(total=Count('date_joined')).filter(userType='Client', date_joined__month=today)
        set = CustomUser.objects.annotate(month=TruncMonth('date_joined')).values('month').annotate(total=Count('date_joined')).filter(userType='Client').values_list('total', flat=True)
        monthSet = CustomUser.objects.filter(userType='Client').annotate(month=TruncMonth('date_joined')).values_list('date_joined__month', flat=True).annotate(total=Count('date_joined__month'))
        arrayTotal = list(set)

        monthTotal = list(monthSet)
        months = []
        for month in sample:
            monthToday = month['month'].strftime('%b')

        context = {
            'qs': qs,
            'set': set,
            'sample': sample,
            'arrayTotal': arrayTotal,
            'monthTotal': monthTotal,
            'months': months,
            'monthToday': monthToday
        }
        return render(request, 'dashboards/views/client_dashboard.html', context)
    else:
        return render(request, 'authentication/views/error.html', {})
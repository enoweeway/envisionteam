from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

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

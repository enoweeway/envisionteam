from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.template.defaultfilters import cut
from django.views.generic import ListView, CreateView
from users.backend import EmailOrUsernameModelBackend

# Create your views here.
from users.models import UserProfile, CustomUser
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.hashers import make_password


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            login(request,user)
            if user.is_superuser:
                return redirect('clientDashboard')
            else:
                return redirect('dashboard')

    context = {
        "form": form
    }

    return render(request, "authentication/views/loginpage.html", context)


def SignUp(request):
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
                    return redirect('users:addUser')
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
                    return redirect('users:addUser')
                else:
                    return render(request, 'authentication/views/error.html', {})
            elif request.user.userType == 'Doctor' or request.user.userType == 'Nurse':
                first_name = request.POST['firstName']
                lower_fname = first_name.replace(" ", "").lower()
                middle_name = request.POST['middleName']
                lower_mname = middle_name.replace(" ", "").lower()
                last_name = request.POST['lastName']
                lower_lname = last_name.replace(" ", "").lower()
                mobileNumber = request.POST['mobile_number']
                hashed_password = make_password(lower_mname)
                username = lower_fname + lower_lname + mobileNumber

                obj = CustomUser.objects.create(
                    username=username,
                    firstName=first_name,
                    middleName=middle_name,
                    lastName=last_name,
                    email=request.POST['email'],
                    mobile_number=mobileNumber,
                    gender=request.POST['gender'],
                    password=hashed_password,
                    userType=request.POST['userType']
                )
                obj.save()
                if request.user.is_authenticated:
                    return redirect('users:addUser')
                else:
                    return render(request, 'authentication/views/error.html', {})
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/views/add_user.html', {'form': form})



class ClientListView(ListView):
    template_name = "clients/views/clients_table.html"
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(userType="Client")
        print(qs)
        context = {
            'qs': qs
        }
        return context


class DoctorListView(ListView):
    template_name = "doctors/views/doctors_table.html"
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(userType="Doctor")
        context = {
            'qs': qs
        }
        return context

class PatientListView(ListView):
    template_name = "patients/views/patients_table.html"
    def get_queryset(self, *args, **kwargs):

        qs = CustomUser.objects.filter(userType="Patient")
        context = {
            'qs': qs
        }
        return context

def edit_profile(request, username):
    if request.user.is_superuser:
        user = CustomUser.objects.get(username=username)
    else:
        user = CustomUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        # print(request.user.is_authenticated())
        if form.is_valid():
            # form.middle_name = request.POST['middle_name']
            # form.profile_image = request.FILES.get('profile_image', user.profile_image)
            form.save()
            return redirect('users:profile', user)
    else:
        form = CustomUserChangeForm(instance=user)
        args = {
            'form': form,
            'user': user
            }
        if user.username == request.user.username or request.user.is_superuser:
            return render(request, 'users/edit_profile.html', args)
        else:
            return render(request, 'authentication/views/error.html', {})

class user_profile(ListView):
    model = UserProfile
    count_hit = True
    template_name = 'users/profile.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    if request.user.username == user.username or request.user.is_superuser or request.user.userType == 'Client' \
            or request.user.userType == 'Doctor' or request.user.userType == 'Nurse':
        return render(request, 'users/profile.html', {"user":user})
    else:
        return render(request, 'authentication/views/error.html', {})

def delete(request, username):
    user = CustomUser.objects.get(username=username)
    if request.user.is_superuser:
        user.delete()
        return redirect('users:clientList')
    elif request.user.userType == 'Client':
        user.delete()
        return redirect('users:doctorList')
    elif request.user.userType == 'Doctor':
        user.delete()
        return redirect('users:patientList')
    else:
        return render(request, 'authentication/views/error.html', {})


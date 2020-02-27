from django.urls import path

from users.views import DoctorListView, PatientListView, ClientListView
from . import views
from django.conf.urls import url
app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    # path('doctors/', views.DoctorListView, name='doctorList'),

    url(r'^clients/', ClientListView.as_view(), name='clientList'),
    url(r'^doctors/', DoctorListView.as_view(), name='doctorList'),
    url(r'^patients/', PatientListView.as_view(), name='patientList'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.get_user_profile, name='profile'),
    path('add_user/', views.SignUp, name='addUser'),
    # url(r'^profile/(?P<username>[\w.@+-]+)/$', views.get_user_profile, name='profile'),
    url(r'^edit/(?P<username>[\w.@+-]+)/$', views.edit_profile, name='edit_profile'),
    # path('edit/', views.edit_profile, name='edit_profile'),
]
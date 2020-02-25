from django.shortcuts import render

def userProfile(request):

    return render(request, 'profile/views/user_profile.html')

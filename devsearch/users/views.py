from django.shortcuts import render, redirect
from .models import Profile
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)

def login_user(request):
    if request.user.is_authenticated:
        redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or Password is incorrect!')

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    return redirect('login')
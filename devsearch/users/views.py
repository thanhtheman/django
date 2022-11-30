from django.shortcuts import render, redirect
from .models import Profile
# from projects.models import Project
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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
    page ='login'
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
            messages.error(request,'Username or Password is incorrect!')

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('login')

def register_user(request):
    page ='register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "An error has occured, please check username & password requirements.")
    context ={'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
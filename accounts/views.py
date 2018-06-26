from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm
from posts.models import Post

# Create your views here.
def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username = login_form.cleaned_data["username"], password = login_form.cleaned_data["password"])
        
            if user is not None:
                auth.login(request, user) # we use auth as we are importing from line 3 and if we don't use auth.login it will conflict like with the logout function underneath
                return redirect("/")
            else:
                login_form.add_error(None, "your username or password are incorrect")
    else:
        login_form = UserLoginForm()
        
    return render(request, "accounts/login.html", {"form": login_form})
    
def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = authenticate(username = registration_form.cleaned_data["username"], password = registration_form.cleaned_data["password1"])
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                registration_form.add_error(None, "can't log in now, try later")
            
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, "accounts/register.html", {"form": registration_form})
    
def logout(request):
    auth.logout(request)
    return redirect('/') 
    
def profile(request):
    return render(request, "accounts/profile.html")
    

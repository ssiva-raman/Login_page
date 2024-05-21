from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

# -- register user and save user 
def register_user(request):
    if request.method=="POST":
        username=request.POST['username']
        email= request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username,email,password1)
            user.save()
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend',)
            return redirect('home')
        else:
            error_message='password not match'
            return render(request, 'html/register.html', {'error_message':error_message} )
    return render(request, 'html/register.html')
        

# -- login user get input from login.html 
def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message='wrong details'
            return render(request, 'html/login.html', {'error_message':error_message} )
    return render(request, 'html/login.html')
            

# -- @ is decoretor without login this view not work 
# -- login url is redirect to login page
@login_required(login_url='login')
def logout_user(request):
    logout(request)     
    return redirect('login')   


# -- landing page after login
@login_required(login_url='login')
def home(request):
    return render(request, 'html/home.html')

    
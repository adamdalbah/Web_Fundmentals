from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from .models import User

def index(request):
    return render(request, "index.html")
def login(request):
    if request.method == "POST":
        if request.POST['login_type'] == "login":
            errors_login = User.objects.login_validator(request.POST)
            if len(errors_login) > 0:
                for key, value in errors_login.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                if models.check_user(request.POST['email'],request.POST['password']):
                    context = {
                            'fname':User.objects.filter(email=request.POST['email']).first()
                    }
                    
                    return render(request,"welcome.html",context)

        

        if request.POST['login_type'] == "registration":
            errors_register = User.objects.validator(request.POST)

            if len(errors_register) > 0:
                for key, value in errors_register.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                models.register(request.POST['fname'], request.POST['lname'],
                request.POST['email'], request.POST['password'], request.POST['cpassword'])
    
    return redirect('/')

# Create your views here.

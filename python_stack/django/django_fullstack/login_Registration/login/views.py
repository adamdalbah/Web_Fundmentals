from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from .models import User
import bcrypt


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
                    if 'name' not in request.session:
                        request.session['name'] = context['fname'].first_name
                    return render(request,"welcome.html",context)
                else: 
                    return redirect("/")

        

        if request.POST['login_type'] == "registration":
            errors_register = User.objects.validator(request.POST)

            if len(errors_register) > 0:
                for key, value in errors_register.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                if request.POST['password'] == request.POST['cpassword']:
                    hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
                    models.register(request.POST['fname'], request.POST['lname'],
                    request.POST['email'], hash)
                    if 'name' not in request.session:
                        request.session['name'] = request.POST['fname']
    
    return redirect('/register')
def logout(request):
    if 'name' in request.session:
        del request.session['name']
    return redirect('/')
def register(request):
    return render(request, "welcome.html")

# Create your views here.

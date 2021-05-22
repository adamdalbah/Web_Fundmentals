from typing import AsyncGenerator, ContextManager
from django.shortcuts import render, redirect, HttpResponse
from .models import User
def index(request):
    context = {
        'users' : User.objects.all() 
    }
    return render(request, "index.html", context)

def add(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],
        email_address=request.POST['email'], age = request.POST['age'])
    return redirect("/")
    


# Create your views here.

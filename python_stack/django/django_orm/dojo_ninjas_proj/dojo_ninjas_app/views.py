from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjaz': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        if request.POST['form'] == 'dojo' :
            Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
        if request.POST['form'] == 'ninja':
            Ninja.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], dojo = Dojo.objects.get(name=request.POST['dojoz']) )



    return redirect('/')



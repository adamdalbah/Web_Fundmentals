from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from .models import Show

# Create your views here.
def shows(request):
    context = {
        "shows" : Show.objects.all(),
    }
    return render(request,'index.html',context)

def index(request):
    return redirect('/shows')

def create(request):
    return render(request,'create_page.html')

def add(request):
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new/")
        else:
            if request.method == "POST":
                Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["date"], description=request.POST["desc"] )
            
            context = {
            "id" : Show.objects.last(),
                }
            return redirect('/shows/'+str(context['id'].id))

def read(request,id):
    context = {
        "shows" : Show.objects.get(id=id),
    }
    return render(request,'read_page.html',context)

def edit(request,id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key , value in errors.items():
            messages.error(request, value)
        return redirect("/shows/"+ str(id) + "/edit/")
    else :
        x= Show.objects.get(id=id)

        if request.method == "POST":
            x.title = request.POST['title']
            x.network = request.POST['network']
            x.description = request.POST['desc']
            x.release_date = request.POST['release_date']
            x.save()


        return redirect("/shows/"+str(id))

def update(request,id):
    context = {
        "shows": Show.objects.get(id=id),
    }
    return render(request,'update_page.html',context)

def destroy(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')


from django.http.response import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    context = {
        'counter': request.session['count'] ,
    }
    return render(request,"index.html", context)
def reset(request):
    request.session.clear()
    return redirect('/')

def add2(request):
    request.session['count'] += 1
    return redirect('/')

def increment(request):
    x = request.POST['increment']
    if x is "":
        request.session['count']-=1
        return redirect('/')
    request.session['count'] += int(x)-1
    return redirect('/')
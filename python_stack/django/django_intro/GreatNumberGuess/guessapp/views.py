from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    request.session['random'] = random.randint(1, 100)
    return render(request, "index.html")

def guess(request):
    if request.POST['num'] is "":
        return redirect('/')
        
    request.session['guess'] = int(request.POST['num'])

    if request.session['guess'] > request.session['random']:
        answer = {
            'result': "Too High!"
        }
        return render(request,"Wresult.html", answer)
    elif request.session['guess'] < request.session['random']:
        answer= {
            'result':"Too Low!"
        }
        return render(request, "Wresult.html", answer)
    else:
        answer ={
            'result': request.session['guess']
        }
        return render(request, "Rresult.html", answer)

        
# Create your views here.

from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    print("Got post info...............")
    name = request.POST['name']
    dojo_location= request.POST['location']
    favorite_language = request.POST['language']
    comment= request.POST['comment']
    results = {
        'name' : name,
        'location':dojo_location,
        'language':favorite_language,
        'comment':comment,
    }
    return render(request,"result.html", results)


# Create your views here.

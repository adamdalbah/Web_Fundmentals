from django.shortcuts import render, HttpResponse
from django.utils import timezone

def index(request):
    context = {
        "time": timezone.now()
    }
    return render(request, 'index.html', context)



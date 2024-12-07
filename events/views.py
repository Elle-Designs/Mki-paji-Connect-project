from django.shortcuts import render, redirect

from events.models import Event 

# Create your views here.

def index(request):
    return render(request 'home.html')

def events(request):
    return render(request 'event.html')





from django.shortcuts import render, redirect

from events.models import Event 

# Create your views here.

def index(request):
    return render(request, 'home.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})









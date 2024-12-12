from django.shortcuts import render, redirect

from events.models import Event 

# Create your views here.

def index(request):
    return render(request, 'home.html')

def events(request):
    # events = Event.objects.all()
    events = {1,2,3,4,5,6,7,8,9,10}
    return render(request, 'events.html', {'events': events})









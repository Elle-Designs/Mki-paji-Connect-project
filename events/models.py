from django.db import models

# Create your models here.

class Event(models.Model): 
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    location = models.CharField
    description = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='event_posters/')
    registration_link = models.URLField()

    def __str__(self):
        return self.name


    

   
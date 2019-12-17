from django.shortcuts import render
from django.http import HttpResponse
from .models import trains
# Create your views here.
def home(request):
    trains = trains.objects.all()

    return render(request, 'home.html', {'trains':trains})
 
    
    
    


    
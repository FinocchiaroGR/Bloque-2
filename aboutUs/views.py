from django.shortcuts import render
from .models import *

# Create your views here.

def AboutUs(request):
    aboutUsArray = SobreNosotros.objects.all()
    
    for i in aboutUsArray:
        about = i
    
    people = Persona.objects.all().order_by('nombre')
        
    
        
    return render(request, "AboutUs/aboutUs.html", {
        "about": about,
        "people": people
    })
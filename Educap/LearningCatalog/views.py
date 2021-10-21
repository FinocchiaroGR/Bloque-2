from django.shortcuts import render
from . import urls

from LearningCatalog.models import Categoria

# Create your views here.

def LearningCatalog(request):
    
    return render(request, "LearningCatalog/primaryCatalog.html",{
        "catalogs": Categoria.objects.all(),
        
    })
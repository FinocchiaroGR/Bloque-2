from django.shortcuts import render
from . import urls

# Create your views here.

def LearningCatalog(request):
    return render(request, "LearningCatalog/primaryCatalog.html",{

    })
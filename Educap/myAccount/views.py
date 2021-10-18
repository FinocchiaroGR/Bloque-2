from django.http.response import HttpResponse
from django.shortcuts import render
from accounts.models import *
# Create your views here.


def studentCreate(request):
    return HttpResponse("Hola")

from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]

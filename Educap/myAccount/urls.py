from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "myAccount"

urlpatterns = [
    path('registroEstudiante/', views.studentCreate, name="studentCreate"),
]

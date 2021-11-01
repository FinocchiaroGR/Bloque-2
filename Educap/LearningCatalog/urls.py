from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "LearningCatalog"

urlpatterns = [
    path('Categorias', views.primaryCategory, name='primaryCategory'),
    path('Categorias/<int:pk>', views.subCategories, name='subCategories')
]

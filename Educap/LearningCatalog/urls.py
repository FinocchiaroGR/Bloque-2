from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "LearningCatalog"

urlpatterns = [
    path('Categorias', views.primaryCategory, name='primaryCategory'),
    path('Categorias/<int:pk>', views.subCategories, name='subCategories'),
    path('Busqueda/Categorias', views.searchCategory, name="searchCategory"),
    path('Lecciones', views.listLesson, name="listLesson"),
    path('Lecciones/<int:pk>', views.readLesson, name="readLesson"),
    path('Buscar/Lecciones', views.searchLesson, name="searchLesson"),
    path('Categoria/Lecciones', views.filterLessonsByCategory,
         name="filterLessonsByCategory"),
]

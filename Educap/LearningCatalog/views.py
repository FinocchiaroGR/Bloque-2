from django.shortcuts import render
from . import urls
from LearningCatalog.models import Categoria
import logging
from .models import *
# Create your views here.


def primaryCategory(request):
    # Respuesta HTTPS donde django procesa el html y presenta la ingerfaz
    return render(request, "LearningCatalog/primaryCategory.html", {
        # Contexto para procesar la interfaz donde se realiza un query a la base de datos y obtenemos todas las categorias
        "categories": Categoria.objects.all(),

    })


def subCategories(request, pk):
    category = Categoria.objects.get(pk=pk)
    subCategory = Categoria.objects.filter(categoriaPadre=category)
    logging.error(subCategory)
    return render(request, "LearningCatalog/subcategory.html", {
        "category": Categoria.objects.get(pk=pk),
        "subCategories": subCategory,
    })


def searchCategory(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/searchBar.html", {
            "categories": Categoria.objects.filter(nombre__icontains=search),
        })


def listLesson(request):
    lessons = Leccion.objects.all()
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })


def readLesson(request, pk):
    lesson = Leccion.objects.get(pk=pk)
    return render(request, "LearningCatalog/lesson.html", {
        "lesson": lesson
    })


def searchLesson(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/lessonList.html", {
            "lessons": Leccion.objects.filter(titulo__icontains=search),
        })


def filterLessonsByCategory(request, pk):
    subCategory = Categoria.objects.get(pk=pk)
    lessons = Leccion.objects.filter(category=subCategory)
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })

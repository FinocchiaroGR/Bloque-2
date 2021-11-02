from django.shortcuts import render
from . import urls
from LearningCatalog.models import Categoria
import logging
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
        logging.error(search)
        return render(request, "LearningCatalog/primaryCategory.html", {
            "categories": Categoria.objects.filter(nombre__icontains=search),
        })

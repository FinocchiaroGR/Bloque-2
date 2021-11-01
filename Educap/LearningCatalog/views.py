from django.shortcuts import render
from . import urls
from LearningCatalog.models import Categoria
import logging
# Create your views here.


def primaryCategory(request):

    return render(request, "LearningCatalog/primaryCategory.html", {
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

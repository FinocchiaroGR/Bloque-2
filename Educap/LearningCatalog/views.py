from django.shortcuts import render
from . import urls

from LearningCatalog.models import Categoria

# Create your views here.


def primaryCategory(request):

    return render(request, "LearningCatalog/primaryCategory.html", {
        "catalogs": Categoria.objects.all(),

    })

from django.contrib.auth.models import User
from django.db import models
from LearningCatalog.models import Categoria
from rest_framework import fields, serializers
from LearningCatalog.models import *


class getLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'descripcion', 'imagen']


class getLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'categoriaPadre']

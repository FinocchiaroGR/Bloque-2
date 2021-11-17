from django.contrib.auth.models import User
from django.db import models
from Educap.LearningCatalog.models import Categoria
from rest_framework import fields, serializers
from LearningCatalog.models import UserModel, Estudiante

class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen','categoriaPadre']
        
    def get():
        return
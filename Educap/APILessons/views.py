from django.conf.urls import handler500
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
import logging
from LearningCatalog.models import *
# Create your views here.


class GetLessonsView(APIView):

    def get(self, request):
        lessons = Leccion.objects.all()
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetLessonView(APIView):

    def get(self, request, id):
        lesson = Leccion.objects.get(id=id)
        serializer = getLessonSerializer(lesson)
        return Response(serializer.data)


class GetCategoryByName(APIView):
    def get(self, request, id):
        category = Categoria.objects.get(id=id)
        serializer = getCategoryById(category)
        return Response(serializer.data)


class GetFilesView(APIView):
    def get(self, request, id):
        files = Archivo.objects.filter(leccion=id)
        serializer = getFilesSerializer(files, many=True)
        return Response(serializer.data)


class GetVideosView(APIView):
    def get(self, request, id):
        videos = Video.objects.filter(leccion=id)
        serializer = getVideosSerializer(videos, many=True)
        return Response(serializer.data)

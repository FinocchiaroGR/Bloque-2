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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lessons = Leccion.objects.all()
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetLessonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        lesson = Leccion.objects.get(id=id)
        serializer = getLessonSerializer(lesson)
        return Response(serializer.data)


class GetCategoryByName(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        category = Categoria.objects.get(id=id)
        serializer = getCategoryById(category)
        return Response(serializer.data)


class GetFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        files = Archivo.objects.filter(leccion=id)
        serializer = getFilesSerializer(files, many=True)
        return Response(serializer.data)


class GetVideosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        videos = Video.objects.filter(leccion=id)
        serializer = getVideosSerializer(videos, many=True)
        return Response(serializer.data)


class GetUserLessons(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        estudiante = Estudiante.objects.get(user=request.user)
        leccion_estudiante = Estudiante_Lecciones.objects.filter(
            estudiante=estudiante)
        lessons = []
        for object in leccion_estudiante:
            lessons.append(object.leccion)
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetLessonsByFilter(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        lessons = Leccion.objects.filter(category=id)
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)

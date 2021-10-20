from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import *
from .forms import *
import logging
# Create your views here.


def studentCreate(request):
    # Metodo post para el registro
    if request.method == "POST":

        # Guardamos formularios con el contenido enviado por el usuario en las variables
        studentFormRequest = StudentForm(request.POST, prefix='student')
        userFormRequest = UserForm(request.POST, prefix='user')

        # Revisamos que los formularios del usuario sea correcto
        if studentFormRequest.is_valid() and userFormRequest.is_valid():

            logging.error("Es valido")

            # Guardado y creacion del nuevo usuario
            # Se guarda el registro de usuario
            userFormRequest.save()
            userFormSave = userFormRequest.save()

            # Se crea el registro del estudiante pero no se guarda
            studentFormSave = studentFormRequest.save(commit=False)
            # Asignamos el usuario al estudiante
            studentFormSave.user = userFormSave
            # Guardamos el estudiante
            studentFormSave.save()
            return redirect('login')
        else:
            logging.error("Es invalido")
            return render(request, "myAccount/studentCreate.html", {
                "studentForm": studentFormRequest,
                "userForm": userFormRequest
            })
    return render(request, "myAccount/studentCreate.html", {
        "studentForm": StudentForm(prefix='student'),
        "userForm": UserForm(prefix='user')
    })

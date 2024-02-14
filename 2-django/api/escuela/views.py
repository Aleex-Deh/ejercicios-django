from django.shortcuts import render
from django.http import JsonResponse
from .models import Escuela
from django.views.decorators.csrf import csrf_exempt
import json
import pdb

# Create your views here.

#Esta función listará todos mis usuarios y contraseñas
def list_alumnos(request):
    
    # Vista para obtener todas las contraseñas y devolverlas en formato JSON.
    titulos = Escuela.objects.all()    # Le asigno el valor de mostrarlo todo. 
    data = [{'titulo': titulo.nombre, 'num_paginas': titulo.dni} for titulo in titulos] # Le asigno el valor del json 
    return JsonResponse({'titulos': data})



@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función añadirá un nuevo usuario.
def add_alumno(request):
 
    data = request.POST
        
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))
    
    nombre = my_json['alumno']
    dni = my_json['dni']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Escuela.objects.create(nombre=nombre, dni=dni)
    return JsonResponse({'Su contraseña se ha guardado con exito' : '.'})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función eliminará el usuario y la contraseña
def delete_alumno(request):
    
    data = request.POST
    
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    nombre = my_json['nombre']
    dni = my_json['dni']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Escuela.objects.filter(nombre=nombre, dni=dni).delete()
    return JsonResponse({'Su contraseña se ha eliminado con exito' : '.'})
from django.shortcuts import render

from django.http import JsonResponse
from .models import Biblioteca
from django.views.decorators.csrf import csrf_exempt
import json
import pdb



#Esta función listará todos mis usuarios y contraseñas
def list_titulos(request):
    
    # Vista para obtener todas las contraseñas y devolverlas en formato JSON.
    titulos = Biblioteca.objects.all()    # Le asigno el valor de mostrarlo todo. 
    data = [{'titulo': titulo.titulo, 'num_paginas': titulo.num_paginas} for titulo in titulos] # Le asigno el valor del json 
    return JsonResponse({'titulos': data})



@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función añadirá un nuevo usuario.
def add_titulo(request):
 
    data = request.POST
        
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))
    
    titulo = my_json['titulo']
    num_paginas = my_json['num_paginas']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Biblioteca.objects.create(titulo=titulo, num_paginas=num_paginas)
    return JsonResponse({'Su contraseña se ha guardado con exito' : '.'})



@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función eliminará el usuario y la contraseña
def delete_titulo(request):
    
    data = request.POST
    
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    titulo = my_json['titulo']
    num_paginas = my_json['num_paginas']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Biblioteca.objects.filter(titulo=titulo, num_paginas=num_paginas).delete()
    return JsonResponse({'Su contraseña se ha eliminado con exito' : '.'})
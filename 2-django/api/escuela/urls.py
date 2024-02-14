from django.urls import path
from . import views

urlpatterns = [
	    path('list-alumnos/', views.list_alumnos, name='list_alumnos'),
     	path('add-alumno/', views.add_alumno, name='add_alumno'),
     	path('delete-alumno/', views.delete_alumno, name='delete_alumno'),

	]

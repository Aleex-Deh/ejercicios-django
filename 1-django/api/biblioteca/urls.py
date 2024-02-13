from django.urls import path
from . import views

# Aquí le asigno una URL a mis funciones dentro del views (.views)

urlpatterns = [
    path('list-titulos/', views.list_titulos, name='list_titulos'),
    path('add-titulo/', views.add_titulo, name='add_password'),
    path('delete-titulo/', views.delete_titulo, name='delete_titulo'),

]
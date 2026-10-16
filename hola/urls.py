from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
    path('nuevo/', views.nuevo_articulo, name='nuevo_articulo'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('articulo/<int:id>/', views.detalle_articulo, name='detalle_articulo'),
    path('articulo/<int:id>/editar/', views.editar_articulo, name='editar_articulo'),  # ← NUEVA
    path('articulo/<int:id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),  # ← NUEVA
    path("contacto/", views.contacto, name="contacto"),
    path("mensajes/", views.ver_mensajes, name="mensajes"),
    path("predecir/", views.predecir_cliente, name="predecir"),
]
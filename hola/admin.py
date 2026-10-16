# hola/admin.py
from django.contrib import admin
from .models import Articulo, Mensaje


class MensajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "fecha_mensaje")

admin.site.register(Articulo)           
admin.site.register(Mensaje, MensajeAdmin)



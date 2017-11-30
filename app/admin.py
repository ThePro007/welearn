# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Maestro, Alumno, Tema , Curso, Pregunta, Categoria, CalificacionTema, Comentario
admin.site.register(Maestro)
admin.site.register(Alumno)
admin.site.register(CalificacionTema)
#admin.site.register(Curso)
admin.site.register(Tema)
admin.site.register(Pregunta)
admin.site.register(Comentario)
#admin.site.register(Categoria)

def publicarCurso(self,request,queryset):
    return queryset.update(status='Publico')

def regresarCurso(self,request,queryset):
    return queryset.update(terminado='')


class AdminCurso(admin.ModelAdmin):
    list_display = ["nombre","dificultad","status","terminado"]
    list_filter = ["nombre","dificultad","status"]
    search_fields = ["nombre","dificultad","status"]
    list_display_links = ["nombre","dificultad","status","terminado"]
    actions = [publicarCurso,regresarCurso]

admin.site.register(Curso,AdminCurso)

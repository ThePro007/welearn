# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings

#Ponemos los Choices de la dificultad del curso
dificultad_curso = (
('1','Principiante'),
('2','Basico'),
('3','Intermedio'),
('4','Avanzado'),
)

status_curso = (
('Publico','Publico'),
)

status_categoria = (
('Aceptado','Aceptado'),
)

terminado = (
('Si','Si'),
)

class Categoria(models.Model):
    categoria = models.CharField(max_length=60)
    status = models.CharField(max_length=25,choices=status_categoria,null=True,blank=True)

    def __str__(self):
        return self.categoria

class Maestro(models.Model):
    name=models.OneToOneField(User)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    foto=models.ImageField(upload_to="images")
    titulo = models.CharField(max_length=300,null=True,blank=True)
    descripcion = models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.name.username

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=30,choices=dificultad_curso)
    foto=models.ImageField(upload_to="images")
    descripcion = models.TextField(max_length=5000)
    maestro = models.ForeignKey(Maestro,on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True,blank=True)
    objetivos = models.TextField(max_length=5000,null=True,blank=True)
    requisitos = models.TextField(max_length=5000,null=True,blank=True)
    status = models.CharField(max_length=30,choices=status_curso,null=True,blank=True)
    terminado = models.CharField(max_length=10,choices=terminado,null=True,blank=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    name=models.OneToOneField(User)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    nivel=models.IntegerField(default=0)#por defecto 0
    foto=models.ImageField(upload_to="images")
    curso = models.ManyToManyField(Curso)

    def __str__(self):
        return self.name.username
'''Sigue pendiente porque no lo corri aveda
class Comentario(models.Model):
    comentario = models.TextField(max_length=270)
    alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE)

    def __str__(self):
        return "%s Alumno que comento"%  self.alumno

class ComentariosCurso(models.Model):
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return self.curso
'''

class CalificacionTema(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tema = models.CharField(max_length = 100)

    def __str__(self):
        return self.tema

class PuntuacionCurso(models.Model):
    puntuacion = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete= models.CASCADE)

    def __str__(self):
        return self.puntuacion

class PuntuacionMaestro(models.Model):
    puntuacion = models.IntegerField()
    maestro = models.ForeignKey(Maestro,on_delete= models.CASCADE)

    def __str__(self):
        return self.puntuacion

class Tema(models.Model):
    nombre = models.CharField(max_length=40)
    teoria = models.TextField(max_length=100000)
    video = models.FileField(blank=True,null=True)
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE)
#    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE)
    contenido = models.TextField(max_length = 500)

    def __unicode__(self):
        return self.contenido

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=270)
    resCorrecta = models.CharField(max_length=100)
    resIncorrecta1 = models.CharField(max_length=100)
    resIncorrecta2 = models.CharField(max_length=100)
    resIncorrecta3 = models.CharField(max_length=100)
    tema = models.ForeignKey(Tema,on_delete = models.CASCADE)

    def __str__(self):
        return self.pregunta

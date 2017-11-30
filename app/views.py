# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView,CreateView #createview
from django.views.generic.list import ListView
from django.views.generic import DetailView,UpdateView

from django.core.urlresolvers import reverse_lazy

from .models import Maestro, Alumno, Curso , Tema ,Pregunta, Categoria, CalificacionTema, Comentario
from .forms import Maestros_Form, Alumnos_Form, Curso_Form, Tema_Form , Pregunta_Form, Categoria_Form, CalificacionTema_form, Comentario_form,Curso_Update_Form, Publicar_Curso_Form

import re
# Create your views here.
def index(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    #Listas los ultimos 3 cursos agregados
    ultCur = Curso.objects.order_by('pk').reverse()[:3]
    #Listas los ultimos 3 tutores agregados
    ultMaes = Maestro.objects.order_by('pk').reverse()[:3]
    #Trae los cursos de la categoria Piropos
    ultCurPir= Curso.objects.raw("select * FROM app_Curso where categoria == 'Piropos' ")

    datos = {'ultCur':ultCur,'ultMaes':ultMaes,'ultCurPir':ultCurPir}

    return render(request,'index.html',{"isTeacher":isTeacher,"current":currentReal,"ultCur":ultCur,'ultMaes':ultMaes})

def empezar_tutor(request):
    return render(request,'empezar_tutor.html')

def bienvenida_tutor(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    current_user = request.user
    userNameMaestro = request.user.username
    mimaestro_id = current_user.id

    maestros=Maestro.objects.all()
    maestro = Maestro.objects.filter(name = mimaestro_id)

    return render(request,'bienvenida_tutor.html',{"isTeacher":isTeacher,"current":currentReal,"maestro":maestro})

def bienvenida_tutor2(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    current_user = request.user
    userNameMaestro = request.user.username
    mimaestro_id = current_user.id

    maestros=Maestro.objects.all()
    maestro = Maestro.objects.filter(name = mimaestro_id)

    return render(request,'bienvenida_tutor2.html',{"isTeacher":isTeacher,"current":currentReal,"maestro":maestro})

def bienvenida_tutor3(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    current_user = request.user
    userNameMaestro = request.user.username
    mimaestro_id = current_user.id

    maestros=Maestro.objects.all()
    maestro = Maestro.objects.filter(name = mimaestro_id)

    return render(request,'bienvenida_tutor3.html',{"isTeacher":isTeacher,"current":currentReal,"maestro":maestro})

def panel_instructor(request):
    return render(request,'panel_instructor.html')

def Signup(request):
    return render(request,'signup.html')

def notificacion_categoria(request):
    return render(request,'notificacion_categoria.html')

class Signup_Maestros(FormView):
    template_name='register.html'
    form_class=Maestros_Form #(request.POST, request.FILES)
    success_url=reverse_lazy('bienvenida_tutor')

    def form_valid(self,form):
        user=form.save()
        p=Maestro()
        p.name=user
        p.nombre=form.cleaned_data["nombre"]
        p.apellido=form.cleaned_data["apellido"]
        p.correo=form.cleaned_data["correo"]
        p.foto=form.cleaned_data["foto"]
        p.save()

        return super(Signup_Maestros,self).form_valid(form)

class Signup_Alumnos(FormView):
    template_name='register.html'
    form_class=Alumnos_Form
    success_url=reverse_lazy('login')

    def form_valid(self,form):
        user=form.save()
        p=Alumno()
        p.name=user
        p.nombre=form.cleaned_data["nombre"]
        p.apellido=form.cleaned_data["apellido"]
        p.correo=form.cleaned_data["correo"]
        p.foto=form.cleaned_data["foto"]
        p.nivel=0
        p.save()

        return super(Signup_Alumnos,self).form_valid(form)

def CategoriaCreate(request):
    if request.method == 'POST':
        form = Categoria_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('notificacion_categoria')
    else:
        form = Categoria_Form()
    return render(request,'categoria_create.html',{'form':form})

# class CursoCreate(CreateView):
#     model=Curso
#     form_class=Curso_Form
#     template_name='curso_form.html'
#     success_url = reverse_lazy('index_view')
def cursoCreate(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    form = Curso_Form(request.POST or None, request.FILES or None)
    curso = Curso()
    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            dificultad = form.cleaned_data['dificultad']
            descripcion = form.cleaned_data['descripcion']
            foto = form.cleaned_data['foto']
            maestroid = request.user.id
            maestro = Maestro.objects.filter(name = maestroid)

            curso.nombre = nombre
            curso.dificultad = dificultad
            curso.descripcion = descripcion
            curso.objetivos = form.cleaned_data['objetivos']
            curso.requisitos = form.cleaned_data['requisitos']
            curso.foto = foto
            curso.maestro = maestro[0]
            curso.save()

            return HttpResponseRedirect('/detail_curso/%i/' % curso.id)
            form = Curso_Form()
    return render(request,'curso/curso_form.html',{'form':form,"isTeacher":isTeacher,"current":currentReal})

def editarCurso(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    objectId=url_objectId(request)

    cursos=Curso.objects.all()
    cursoActual=[]
    for curso in cursos:
        if curso.id == objectId:
            cursoActual=curso

    form = Curso_Update_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            cursoActual.nombre= form.cleaned_data['nombre']
            cursoActual.descripcion = form.cleaned_data['descripcion']
            cursoActual.objetivos = form.cleaned_data['objetivos']
            cursoActual.requisitos = form.cleaned_data['requisitos']
            #cursoActual.status = form.cleaned_data['status']

            cursoActual.save()

            return HttpResponseRedirect('/detail_curso/%i/' % cursoActual.id)

            form = Curso_Update_Form()

    return render(request,'curso/update_curso.html',{'form':form,"isTeacher":isTeacher,"current":currentReal,"cursoActual":cursoActual})


def publicarCurso(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    objectId=url_objectId(request)

    cursoActual=[]
    cursos=Curso.objects.all()
    for curso in cursos:
        if curso.id == objectId:
            cursoActual=curso

    form = Publicar_Curso_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cursoActual.terminado = form.cleaned_data['terminado']

            cursoActual.save()

            return HttpResponseRedirect('/detail_curso/%i/' % cursoActual.id)

            form = Publicar_Curso_Form()

    return render(request,'curso/publicar_curso.html',{'form':form,"isTeacher":isTeacher,"current":currentReal,"cursoActual":cursoActual})


def temaCreate(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

        form = Tema_Form(request.POST or None, request.FILES or None)
        tema = Tema()
        if request.method == 'POST':
            if form.is_valid():

                # nombre = form.cleaned_data['nombre']
                # teoria = form.cleaned_data['teoria']
                # video = form.cleaned_data['video']
                # curso = models.ForeignKey(Curso,on_delete = models.CASCADE)

                tema.nombre = form.cleaned_data['nombre']
                tema.teoria = form.cleaned_data['teoria']
                tema.video = form.cleaned_data['video']

                objectId=url_objectId(request)
                cursos=Curso.objects.all()
                for curso in cursos:
                    if curso.id == objectId:
                        tema.curso = curso

                tema.save()
                return HttpResponseRedirect('/detail_tema/%i/' % tema.id)
                form = Tema_Form()
        return render(request,'tema/tema_form.html',{'form':form,"isTeacher":isTeacher,"current":currentReal})

def ListMaestros(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    return render(request,'list_maestro.html',{"isTeacher":isTeacher,"current":currentReal,"object_list":Maestro.objects.all()})


class ListViewAlumno(ListView):
    model=Alumno
    template_name='list_alumno.html'

def ListCursos(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    return render(request,'curso/list_curso.html',{"isTeacher":isTeacher,"current":currentReal,"object_list":Curso.objects.all()})



class ListarCategoria(ListView):
    model=Categoria
    template_name='listar_categoria.html'

class ListViewTema(ListView):
    model=Tema
    template_name='list_tema.html'

def CursoDetail(request):
    current=request.user.username
    isTeacher=False
    esPropietario=False
    currentReal=""
    objectId=url_objectId(request)# Este es el id que recibe de la URL

    cursos=Curso.objects.all()
    cursoActual=0
    for cursoObject in cursos:
        if cursoObject.id == objectId:
            cursoActual=cursoObject     #Curso Actual

    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
            if cursoActual.maestro==teacher:
                esPropietario=True

    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual


    suscrito=False
    if isTeacher==False and currentReal != "": #Metodo para ver si ya esta suscrito
        alumnoActual=currentReal
        cursosSuscritos=alumnoActual.curso.all()

        for cursoSuscrito in cursosSuscritos:
            if cursoSuscrito.id == objectId:
                suscrito=True


    if request.method == 'POST': #Metodo para suscribirse
        alumnoActual=currentReal #Alumno Actual

        if suscrito==True:
            alumnoActual.curso.remove(cursoActual)
        else:
            alumnoActual.curso.add(cursoActual)
        return HttpResponseRedirect('/perfil_alumno/')


    temas=Tema.objects.all()# Este metodo es para Temas del curso actual
    temasActuales=[]
    for tema in temas:
        if tema.curso.id==objectId:
            temasActuales.append(tema)

    return render(request,'curso/detailCurso.html',{"isTeacher":isTeacher,"esPropietario":esPropietario,"current":currentReal,"objectId":objectId,"cursos":Curso.objects.all(),"isSubscribed":suscrito,"temas":temasActuales})




def temaDetail(request):
    cursosSuscritos = 'nunguno';
    current=request.user.username
    isTeacher=False
    esPropietario=False
    currentReal=""
    objectId=url_objectId(request)# Este es el id que recibe de la URL

    temas=Tema.objects.all()
    temaActual=0
    for tema in temas:
        if tema.id==objectId:
            temaActual=tema

    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
            if temaActual.curso.maestro==teacher:
                esPropietario=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    if isTeacher==False and current!="": #Metodo para ver si ya esta suscrito
        alumnoActual=currentReal
        cursosSuscritos=alumnoActual.curso.all()

    calificacionesTema = CalificacionTema.objects.all()

    #Formulario para almacenar resultados del test del tema----------------
    form = CalificacionTema_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            existe = False
            alumnoCalificacion = form.cleaned_data['alumno']
            temaCalificacion =  form.cleaned_data['tema']
            calificacionCalificacion  = form.cleaned_data['calificacion']

            calificacionTema = CalificacionTema()
            calificacionTema.tema = temaCalificacion
            calificacionTema.calificacion = calificacionCalificacion
            for alumno in Alumno.objects.all():
                alumnoPk = int(alumno.id)
                if alumnoPk == alumnoCalificacion:
                    calificacionTema.alumno = alumno

            calificacionTemaTemp = CalificacionTema.objects.all()
            for i in calificacionTemaTemp:
                if i.alumno == calificacionTema.alumno:
                    if i.tema == temaCalificacion:
                        existe = True
                        i.calificacion = calificacionCalificacion
                        i.save()

            if not existe:
                calificacionTema.save()

            form = CalificacionTema_form
        #Fin del formulario-----------------------------------------

    #Formulario para comentario
    form2 = Comentario_form(request.POST or None)
    if request.method == 'POST' and 'btnSubmit' in request.POST:
        if form2.is_valid():
            comentario = Comentario()
            alumnoId = form2.cleaned_data['alumno']
            temaId = form2.cleaned_data['tema']
            comentario.contenido = form2.cleaned_data['contenido']


            for alumno in Alumno.objects.all():
                alumnoPk = int(alumno.id)
                if alumnoPk == alumnoId:
                    comentario.alumno = alumno

            for tema in Tema.objects.all():
                temaPk = int(tema.id)
                if temaPk == temaId:
                    comentario.tema = tema

            comentario.save()
            form2 = Comentario_form()
    #-------------------------

    comentariosTema = Comentario.objects.all()

    preguntas=Pregunta.objects.all()
    preguntasActuales=[]
    for pregunta in preguntas:
        if pregunta.tema.id == objectId:
            preguntasActuales.append(pregunta)
    hayPreguntas=True
    if len(preguntasActuales) == 0:
        hayPreguntas=False


    return render(request,'tema/detailTema.html',{"isTeacher":isTeacher,"esPropietario":esPropietario,"current":currentReal,"objectId":objectId,"temas":Tema.objects.all(),"cursosSuscritos":cursosSuscritos,"preguntas":preguntasActuales,"hayPreguntas":hayPreguntas,"form":form,"form2":form2,"calificacionesTema":calificacionesTema,'comentariosTema':comentariosTema})

def editarTema(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    objectId=url_objectId(request)# Este es el id que recibe de la URL
    temaActual=[]
    temas=Tema.objects.all()
    for tema in temas:
        temaid=int(tema.id)
        if temaid == objectId:
            temaActual=tema

    form = Tema_Form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():

            temaActual.nombre= form.cleaned_data['nombre']
            temaActual.teoria = form.cleaned_data['teoria']
            videoNuevo = form.cleaned_data['video']

            if videoNuevo != None:
                temaActual.video = videoNuevo

            temaActual.save()

            return HttpResponseRedirect('/detail_tema/%i/' % temaActual.id)

            form = Tema_Form()

    return render(request,'tema/update_tema.html',{'form':form,"isTeacher":isTeacher,"current":currentReal,"temaActual":temaActual})


def tutorDetail(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

    objectId=url_objectId(request)# Este es el id que recibe de la URL

    listaCursos = []
    cursos = Curso.objects.all()

    current_user = request.user
    userNameMaestro = request.user.username
    mimaestro_id = current_user.id

    maestros=Maestro.objects.all()
    maestro = Maestro.objects.filter(name = mimaestro_id)

    for curso in cursos:
        if objectId == curso.maestro.id:
            listaCursos.append(curso)

    return render(request,'detailTutor.html',{"isTeacher":isTeacher,"current":currentReal,"objectId":objectId,"maestros":Maestro.objects.all(),'cursos':listaCursos,'cantidad_cursos':len(listaCursos)})


def perfil_alumno(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual
    #------------------------------
    current_user = request.user
    alumno_id = current_user.id

    alumnos=Alumno.objects.all()
    alumno = Alumno.objects.filter(name = alumno_id)
    return render(request,'perfil_alumno.html', {"isTeacher":isTeacher,"current":currentReal,'alumno':alumno})

def perfil_maestro(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual
    #---------------------
    current_user = request.user
    userNameMaestro = request.user.username
    mimaestro_id = current_user.id

    maestros=Maestro.objects.all()
    maestro = Maestro.objects.filter(name = mimaestro_id)

    listaCursos = []
    cursos = Curso.objects.all()

    for curso in cursos:
        if userNameMaestro == str(curso.maestro):
            listaCursos.append(curso)
    return render(request,'perfil_maestro.html',{"isTeacher":isTeacher,"current":currentReal,'maestro':maestro,'cursos':listaCursos,'cantidad_cursos':len(listaCursos)})


def preguntaCreate(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual

        form = Pregunta_Form(request.POST or None, request.FILES or None)
        pregunta = Pregunta()
        if request.method == 'POST':
            if form.is_valid():

                # nombre = form.cleaned_data['nombre']
                # teoria = form.cleaned_data['teoria']
                # video = form.cleaned_data['video']
                # curso = models.ForeignKey(Curso,on_delete = models.CASCADE)

                pregunta.pregunta = form.cleaned_data['pregunta']
                pregunta.resCorrecta = form.cleaned_data['resCorrecta']
                pregunta.resIncorrecta1 = form.cleaned_data['resIncorrecta1']
                pregunta.resIncorrecta2 = form.cleaned_data['resIncorrecta2']
                pregunta.resIncorrecta3 = form.cleaned_data['resIncorrecta3']

                objectId=url_objectId(request)# Este es el id que recibe de la URL

                temas=Tema.objects.all()
                for tema in temas:
                    if tema.id == objectId:
                        pregunta.tema = tema

                pregunta.save()
                return HttpResponseRedirect('/detail_tema/%i/' % objectId)
                form = Pregunta_Form()
        return render(request,'pregunta_form.html',{'form':form,"isTeacher":isTeacher,"current":currentReal})

def editarPregunta(request):
    current=request.user.username
    isTeacher=False
    currentReal=""
    teachers=Maestro.objects.all()
    for teacher in teachers:
        nombre=str(teacher.name)
        if current == nombre:
            currentReal=teacher #En esta variable se guarda el objeto actual
            isTeacher=True
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        nombre=str(alumno.name)
        if current == nombre:
            currentReal=alumno #En esta variable se guarda el objeto actual


    objectId=url_objectId(request)# Este es el id que recibe de la URL
    preguntas=Pregunta.objects.all()
    for pregunta in preguntas:
        preguntaid=pregunta.id
        if preguntaid == objectId:
            preguntaActual=pregunta

    form = Pregunta_Form(request.POST or None, request.FILES or None)
    pregunta = Pregunta()
    if request.method == 'POST':
        if form.is_valid():

            preguntaActual.pregunta = form.cleaned_data['pregunta']
            preguntaActual.resCorrecta = form.cleaned_data['resCorrecta']
            preguntaActual.resIncorrecta1 = form.cleaned_data['resIncorrecta1']
            preguntaActual.resIncorrecta2 = form.cleaned_data['resIncorrecta2']
            preguntaActual.resIncorrecta3 = form.cleaned_data['resIncorrecta3']


            preguntaActual.save()
            return HttpResponseRedirect('/detail_tema/%i/' % preguntaActual.tema.id)
            form = Pregunta_Form()
    return render(request,'update_pregunta.html',{'form':form,"isTeacher":isTeacher,"current":currentReal,"preguntaActual":preguntaActual})


def json_tema(request):
    data = serializers.serialize('json',Tema.objects.all())
    return HttpResponse(data,content_type = 'application/json')


####################################################
########  Metodos repetidos                   ######
####################################################

def url_objectId(request):
    objectId=0
    urlActual=request.path
    pattern=r"([0-9]+)"

    match=re.search(pattern,urlActual)
    if match:
        objectId=int(match.group())
        return objectId
    return objectId

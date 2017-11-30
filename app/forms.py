from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import dificultad_curso,terminado
from .models import Maestro, Alumno, Curso, Tema , Pregunta, Categoria


status_curso = (
('Publico','Publico'),
)

terminado = (
('Si','Si'),
)

class Categoria_Form(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = ['categoria',]

class Maestros_Form(UserCreationForm):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    correo=forms.CharField(max_length=30)
    foto=forms.ImageField()


class Alumnos_Form(UserCreationForm):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    correo=forms.CharField(max_length=30)
    foto=forms.ImageField()

class Curso_Form(forms.Form):
    nombre = forms.CharField(max_length = 50)
    dificultad = forms.ChoiceField(choices = dificultad_curso, widget=forms.Select(), required=True)
    foto = forms.ImageField()
    descripcion = forms.CharField(max_length=5000,required=False)
    objetivos = forms.CharField(max_length=5000,required=False)
    requisitos = forms.CharField(max_length=5000,required=False)
    #status= forms.ChoiceField(choices=status_curso)

class Curso_Update_Form(forms.Form):
    nombre = forms.CharField(max_length = 50)
    descripcion = forms.CharField(max_length=5000,required=False)
    objetivos = forms.CharField(max_length=5000,required=False)
    requisitos = forms.CharField(max_length=5000,required=False)
    #status= forms.ChoiceField(choices=status_curso,required=False)

class Publicar_Curso_Form(forms.Form):
    terminado= forms.ChoiceField(choices=terminado,required=False)

    # class Meta:
    #     model = Curso
    #
    #     fields = [
    #         'nombre',
    #         'dificultad',
    #         'descripcion',
    #         'foto',
    #     ]

#class CursoFormUpdate(forms.Form):
    #descripcion = forms.CharField(max_length=5000,required=False)
    #objetivos = forms.CharField(max_length=5000,required=False)
    #requisitos = forms.CharField(max_length=5000,required=False)

class Tema_Form(forms.Form):
    nombre = forms.CharField(max_length=40)
    teoria = forms.CharField(widget=forms.Textarea)
    video = forms.FileField(required=False)

class Pregunta_Form(forms.Form):
    pregunta = forms.CharField(max_length=270)
    resCorrecta = forms.CharField(max_length=100)
    resIncorrecta1 = forms.CharField(max_length=100)
    resIncorrecta2 = forms.CharField(max_length=100)
    resIncorrecta3 = forms.CharField(max_length=100)

        # fields = [
        # 'pregunta',
        # 'resCorrecta',
        # 'resIncorrecta1',
        # 'resIncorrecta2',
        # 'resIncorrecta3',
        # 'tema'
        # ]
        #
        # labels = {
        #     'pregunta ': 'Ingrese pregunta: ',
        #     'resCorrecta':'Respuesta (correcta)',
        #     'resIncorrecta1':'Respuesta (incorrecta)',
        #     'resIncorrecta2':'Respuesta (incorrecta)',
        #     'resIncorrecta3':'Respuesta (incorrecta)',
        #     'tema':'Selecione el cuestionario al que pertenece'
        # }

class CalificacionTema_form(forms.Form):
    alumno = forms.IntegerField()
    tema = forms.CharField(max_length = 100)
    calificacion = forms.DecimalField(max_digits=5, decimal_places=2)

class Comentario_form(forms.Form):
    alumno = forms.IntegerField()
    tema = forms.IntegerField()
    contenido = forms.CharField(widget=forms.Textarea,label='', max_length = 500)

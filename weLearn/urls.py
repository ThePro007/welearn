"""weLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views

from django.contrib.auth.views import login,logout_then_login,logout

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    ####################################################
    ########  Login / Registro / Index / Admin   ######
    ####################################################

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index_view"),
    url(r'^login/',login,{"template_name":'login.html'},name="login"),
    url(r'^cerrar/$',logout_then_login,name='logout'),
    url(r'^signup/$',views.Signup,name="Signup_view"),
    url(r'^signup1/$',views.Signup_Maestros.as_view(),name="Signup1_view"),
    url(r'^signup2/$',views.Signup_Alumnos.as_view(),name="Signup2_view"),

    ####################################################
    ########  ALumnos / Maestros                   ######
    ####################################################

    url(r'^perfil_alumno/$',views.perfil_alumno),
    url(r'^perfil_maestro/$',views.perfil_maestro),
    url(r'^listar_maestro/$',views.ListMaestros,name="listar_maestro"),

    ####################################################
    ########  Cursos                            ######
    ####################################################

    url(r'^crea_curso/$',views.cursoCreate,name="crea_curso"),
    url(r'^detail_curso/[0-9]+/$',views.CursoDetail,name = 'curso_detail_view'),
    url(r'^listar_curso/$',views.ListCursos,name="listar_curso"),
    url(r'^editar_curso/[0-9]+/$',views.editarCurso,name="editar_curso"),
    url(r'^publicar_curso/[0-9]+/$',views.publicarCurso,name="publicar_curso"),

    ####################################################
    ########  temas                               ######
    ####################################################

    url(r'^crea_tema/[0-9]+$',views.temaCreate,name="crea_tema"),
    url(r'^detail_tema/[0-9]+/$',views.temaDetail,name = 'tema_detail_view'),
    url(r'^editar_tema/[0-9]+/$',views.editarTema,name="editar_tema"),
    url(r'^json_tema/$',views.json_tema, name = 'json_tema_view'),

    ####################################################
    ########  Preguntas                            ######
    ####################################################


    url(r'^crea_pregunta/[0-9]+$',views.preguntaCreate,name="crea_pregunta"),
    url(r'^editar_pregunta/[0-9]+/$',views.editarPregunta,name="editar_Pregunta"),

    ####################################################
    ########  Tutor                               ######
    ####################################################

    url(r'^detail_tutor/[0-9]+/$',views.tutorDetail,name = 'tutor_detail_view'),
    url(r'^empezar_tutor/$',views.empezar_tutor,name="empezar_tutor"),
    url(r'^bienvenida_tutor/$',views.bienvenida_tutor,name="bienvenida_tutor"),
    url(r'^bienvenida_tutor2/$',views.bienvenida_tutor2,name="bienvenida_tutor2"),
    url(r'^bienvenida_tutor3/$',views.bienvenida_tutor3,name="bienvenida_tutor3"),
    #url(r'^panel_instructor/$',views.panel_instructor,name="panel_instructor"),

    ####################################################
    ########  Categoria                           ######
    ####################################################

    url(r'^crear_categoria/$',views.CategoriaCreate,name="crear_categoria"),
    url(r'^notificacion_categoria/$',views.notificacion_categoria,name="notificacion_categoria"),
    url(r'^listar_categoria/$',views.ListarCategoria.as_view(),name="listar_categoria"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

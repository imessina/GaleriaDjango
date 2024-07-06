from django.urls import path
from .views import index, crud,alumnos_findEdit
from galeria import views

urlpatterns = [
    #Htmls
    path('', views.index, name='index'),
    path('anime/', views.anime, name='anime'),
    path('games/', views.games, name='games'),
    path('contacto/', views.contacto, name='contacto'),
    path('comprar/', views.comprar, name='comprar'),
    path('polera1/', views.polera1, name='polera1'),
    path('polera2/', views.polera2, name='polera2'),
    path('polera3/', views.polera3, name='polera3'),
    path('polera4/', views.polera4, name='polera4'),
    path('api/', views.api, name='api'),
    path('rock/', views.rock, name='rock'),
    
    #clientes

    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),
    path('clientes/nuevo/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),

    #contacto
    path('contacto/', views.contacto_crear, name='contacto_crear'),
    path('contacto/exito/', views.contacto_exito, name='contacto_exito'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),


    #Crud

    path('crud', views.crud, name='crud'),
    path('galeria/alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('galeria/alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('galeria/alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('galeria/alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
    path('galeria/alumnosAdd/', views.alumnosAdd, name='alumnos_add'),
]


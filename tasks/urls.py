from django.urls import path
from . import views # Importa las vistas de la app

# Este 'app_name' es útil para organizar
app_name = 'tasks'

urlpatterns = [
    # URL para la lista de proyectos: /
    path('', views.project_list, name='project-list'),

    # URL para el detalle: /proyecto/1/ (el <int:pk> es un parámetro dinámico)
    path('proyecto/<int:pk>/', views.project_detail, name='project-detail'),
]
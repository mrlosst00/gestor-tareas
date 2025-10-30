from django.urls import path
from . import views # Importa las vistas de la app

# Este 'app_name' es útil para organizar
app_name = 'tasks'

urlpatterns = [
    path('', views.project_list, name='project-list'),
    path('proyecto/<int:pk>/', views.project_detail, name='project-detail'),

    # --- AÑADE ESTA LÍNEA ---
    # La URL será algo como /proyecto/1/nueva-tarea/
    path('proyecto/<int:project_pk>/nueva-tarea/', views.task_create, name='task-create'),
]
from django.shortcuts import render, get_object_or_404
from .models import Project, Task # Importamos nuestros modelos

# Vista para mostrar la lista de TODOS los proyectos
def project_list(request):
    # 1. Obtener todos los objetos Project de la BD
    projects = Project.objects.all()

    # 2. Enviar esos datos a una plantilla HTML
    # 'context' es un diccionario que pasa datos de Python a HTML
    context = {
        'projects': projects
    }
    return render(request, 'tasks/project_list.html', context)

# Vista para mostrar el detalle de UN proyecto y sus tareas
def project_detail(request, pk):
    # 1. Obtener UN proyecto por su Primary Key (pk), o mostrar un error 404 si no existe
    project = get_object_or_404(Project, pk=pk)

    # 2. Enviar ese proyecto a la plantilla
    context = {
        'project': project
    }
    return render(request, 'tasks/project_detail.html', context)
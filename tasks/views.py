from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task 
from .forms import TaskForm # Importamos nuestros modelos

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

def task_create(request, project_pk):
    # Primero, obtenemos el proyecto al que pertenecerá esta tarea
    project = get_object_or_404(Project, pk=project_pk)

    # Comprobamos si el formulario se está enviando (POST)
    if request.method == 'POST':
        form = TaskForm(request.POST) # Llenamos el formulario con los datos enviados

        if form.is_valid(): # Django valida los datos por nosotros
            # El formulario es válido. PERO no lo guardes todavía.
            task = form.save(commit=False) # commit=False nos da el objeto sin guardarlo en BD

            # --- AQUÍ LA CLAVE ---
            # Asignamos el proyecto manualmente
            task.project = project 

            # Ahora sí, guardamos el objeto completo en la BD
            task.save()

            # Redirigimos al usuario de vuelta a la lista de tareas de ese proyecto
            return redirect('tasks:project-detail', pk=project.pk)

    # Si no es POST, es un GET, así que solo mostramos un formulario vacío
    else:
        form = TaskForm()

    # Preparamos el contexto para la plantilla
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'tasks/task_form.html', context)

# ... (tus otras importaciones: render, get_object_or_404, redirect, Task, Project, TaskForm)

def task_update(request, project_pk, task_pk):
    # 1. Obtenemos la tarea específica que queremos editar
    task = get_object_or_404(Task, pk=task_pk, project__pk=project_pk)

    # 2. Comprobamos si es POST (guardando cambios)
    if request.method == 'POST':
        # 3. Llenamos el formulario con los datos POST y le decimos QUÉ INSTANCIA actualizar
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save() # Como es un ModelForm, solo hay que guardar
            return redirect('tasks:project-detail', pk=project_pk)

    # 4. Si es GET (cargando la página), llenamos el formulario con los datos de la tarea existente
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'project': task.project, # Pasamos el proyecto de la tarea
        'task': task # Pasamos la tarea para poder diferenciar el título
    }
    # 5. ¡REUTILIZAMOS LA PLANTILLA! No necesitamos crear un HTML nuevo.
    return render(request, 'tasks/task_form.html', context)

# ... (tus otras vistas)

def task_delete(request, project_pk, task_pk):
    task = get_object_or_404(Task, pk=task_pk, project__pk=project_pk)

    # Por seguridad, solo borramos si es una petición POST
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:project-detail', pk=project_pk)

    # Si es GET, mostramos la página de confirmación
    context = {
        'task': task,
        'project': task.project
    }
    return render(request, 'tasks/confirm_delete.html', context)
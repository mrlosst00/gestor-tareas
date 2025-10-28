from django.db import models

# Modelo para Proyectos
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) # blank=True (opcional en formularios), null=True (opcional en BD)

    # Esto ayuda a que en el panel de admin se vea el nombre y no "Project object (1)"
    def __str__(self):
        return self.name

# Modelo para Tareas
class Task(models.Model):
    # Opciones para el campo 'status'
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('IN_PROGRESS', 'En Progreso'),
        ('COMPLETED', 'Completada'),
    ]

    title = models.CharField(max_length=150)

    # --- LA LÍNEA MÁS IMPORTANTE ---
    # Esto crea la relación. Cada Tarea se vincula a un Proyecto.
    # on_delete=models.CASCADE: Si un Proyecto se borra, todas sus tareas se borran.
    # related_name='tasks': Nos permitirá hacer `proyecto.tasks.all()` más adelante.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.title
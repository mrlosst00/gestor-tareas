from django.contrib import admin
from .models import Project, Task  # 1. Importa tus modelos

# 2. Regístralos en el sitio de admin
admin.site.register(Project)
admin.site.register(Task)
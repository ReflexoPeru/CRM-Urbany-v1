import os
from celery import Celery

# Establecer el módulo de configuración de Django predeterminado para el programa 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usar una cadena aquí significa que el trabajador no tiene que serializar
# el objeto de configuración a objetos hijos.
# - namespace='CELERY' significa que todas las claves de configuración de celery
#   deben tener un prefijo `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar módulos de tareas de todas las configuraciones de aplicaciones Django registradas.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

app = Celery("server", backend='redis://redis:6379/0')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appbackend.settings")

app = Celery("appbackend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
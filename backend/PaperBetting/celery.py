import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PaperBetting.settings")

app = Celery("PaperBetting")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
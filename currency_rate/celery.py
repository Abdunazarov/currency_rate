from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# переменная окружения для celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_rate.settings")

app = Celery("PhotoPoint")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

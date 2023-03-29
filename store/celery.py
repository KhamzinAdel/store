import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-1st-day-month': {
        'task': 'users.tasks.send_beat_email',
        'schedule': crontab(0, 0, day_of_month='1'),
    }
}

# from celery import task
# from .models import Poliza
from celery.task.schedules import crontab
from celery.decorators import periodic_task






@periodic_task(run_every=(crontab()), name="test", ignore_result=False)
def print_algo():
	print('pollo')
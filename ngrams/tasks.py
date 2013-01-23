import os
import re

from celery import task,chord,group,chain
from celery.signals import task_success
from celery.utils.log import get_task_logger

from django.conf import settings

from .models import *

@task()
def reset_trigrams():
    files = os.listdir(settings.TRIGRAM_PATH)
    c2 = chord(delete_all.si())(group([load_trigram_file.si(f) for f in files]))
    res = c2()
    res.get()


@task()
def delete_all():
    Trigram.objects.all().delete()

@task()
def load_trigram_file(f):
    trgs = []
    with open(os.path.join(settings.TRIGRAM_PATH,f),'r') as file_handle:
        for line in file_handle:
            l = line.strip().split("\t")
            words = l[0].split(" ")
            trgs.append([Trigram(Word=words[-1],word_i_minus_one=words[1],word_i_minus_two=words[0],count=int(l[1]))]
    if trgs != []:
        Trigram.objects.bulk_create(trgs)

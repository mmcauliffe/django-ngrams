import os
import re

from celery import task,chord,group,chain
from celery.signals import task_success
from celery.utils.log import get_task_logger

from django.conf import settings

from .models import *

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

@task()
def reset_trigrams():
    files = sorted(os.listdir(settings.TRIGRAM_PATH))
    ajob = group([load_trigrams.si(x) for x in chunks(files,25)])
    c2 = (delete_all.si() | ajob)
    res = c2()
    res.get()


@task()
def delete_all():
    Trigram.objects.all().delete()


@task()
def load_trigrams(files):
    for f in files:
        print f
        #est_load(f)
        load_trigram_file(f)

def test_load(f):
    trgs = []
    with open(os.path.join(settings.TRIGRAM_PATH,f),'r') as file_handle:
        found = False
        for line in file_handle:
            if found:
                continue
            found = True
            print line
            l = line.strip().split("\t")
            print l
            words = l[0].split(" ")
            print words
            ws = Orthography.objects.filter(spelling__in = words)
            print ws
            lookedUp = []
            for i in range(len(words)):
                for s in ws:
                    if words[i] == s.spelling:
                        lookedUp.append(s)
                        break
            print lookedUp
            trgs.append(Trigram(word=lookedUp[-1],word_i_minus_one=lookedUp[1],word_i_minus_two=lookedUp[0],count=int(l[1])))
            print trgs


def load_trigram_file(f):
    trgs = []
    with open(os.path.join(settings.TRIGRAM_PATH,f),'r') as file_handle:
        for line in file_handle:
            l = line.strip().split("\t")
            words = l[0].split(" ")
            ws = Orthography.objects.filter(spelling__in = words)
            lookedUp = []
            for i in range(len(words)):
                for s in ws:
                    if words[i] == s.spelling:
                        lookedUp.append(s)
                        break
            trgs.append(Trigram(word=lookedUp[-1],word_i_minus_one=lookedUp[1],word_i_minus_two=lookedUp[0],count=int(l[1])))
            if len(trgs) % 1000 == 0:
                print len(trgs)
            if len(trgs) > 100000:
                Trigram.objects.bulk_create(trgs)
                trgs = []
    if trgs != []:
        Trigram.objects.bulk_create(trgs)

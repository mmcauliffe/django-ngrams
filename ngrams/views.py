# Create your views here.
import os,csv

from django.core.management import call_command
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from .tasks import reset_trigrams

@login_required
def index(request):
    return render(request,'ngrams/index.html',{})

@login_required
def reset(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ResetForm(request.POST)
            if form.is_valid():
                reset_trigrams.delay()
                return redirect(index)
            else:
                form = ResetForm()
                render(request,'ngrams/form.html',{'form':form})
        form = ResetForm()
        return render(request,'ngrams/form.html',{'form':form})


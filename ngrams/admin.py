'''
Created on 2012-07-17

@author: michael
'''
from models import *
from forms import *
from django.contrib import admin


class TrigramAdmin(admin.ModelAdmin):
    model = Trigram
    list_display = ('word_i_minus_one','word_i_minus_two','word','count')

admin.site.register(Trigram, TrigramAdmin)

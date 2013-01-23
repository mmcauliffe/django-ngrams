'''
Created on 2012-07-16

@author: michael
'''
from django import forms

class ResetForm(forms.Form):
    reset = forms.BooleanField(initial=True,required=False)

'''
Created on 2012-07-16

@author: michael
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('ngrams.views',
    (r'^$','index'),
    (r'^reset/$','reset'),
)

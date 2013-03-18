from django.db import models
# Create your models here.

from celex.models import Orthography

import caching.base

class Trigram(caching.base.CachingMixin, models.Model):
    word = models.ForeignKey(Orthography,related_name='word')
    word_i_minus_one = models.ForeignKey(Orthography,related_name='word_i_minus_one')
    word_i_minus_two = models.ForeignKey(Orthography,related_name='word_i_minus_two')
    count = models.IntegerField()

    objects = caching.base.CachingManager()

    def get_context(self):
        return u'%s %s' % (self.word_i_minus_two,self.word_i_minus_one)

class Bigram(models.Model):
    word = models.CharField(max_length=250)
    word_i_minus_one = models.CharField(max_length=250)
    count = models.IntegerField()

    def get_context(self):
        return u'%s' % (self.word_i_minus_one)

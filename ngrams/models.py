from django.db import models
# Create your models here.


class Trigram(models.Model):
    word = models.CharField(max_length=250)
    word_i_minus_one = models.CharField(max_length=250)
    word_i_minus_two = models.CharField(max_length=250)
    count = models.IntegerField()
    objects = TrigramManager()

class Bigram(models.Model):
    word = models.CharField(max_length=250)
    word_i_minus_one = models.CharField(max_length=250)
    count = models.IntegerField()
    objects = BigramManager()

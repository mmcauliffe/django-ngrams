import math
import os

from .models import *

def in_trigram_context_entropy(wordOne,wordTwo):
    if type(wordOne) == type([]):
        w_one = Trigram.objects.filter(word__spelling__in=wordOne)
        w_two = Trigram.objects.filter(word__spelling__in=wordTwo)
    else:
        w_one = Trigram.objects.filter(word__spelling=wordOne)
        w_two = Trigram.objects.filter(word__spelling=wordTwo)

    w_one_contexts = {x.get_context(): x.count for x in w_one}
    w_two_contexts = {x.get_context(): x.count for x in w_two}
    w_one_contexts.update({x:0 for x in w_two_contexts if x not in w_one_contexts})
    w_two_contexts.update({x:0 for x in w_one_contexts if x not in w_two_contexts})
    #print(w_one_contexts)
    #print(w_two_contexts)
    #print w_one_contexts
    #print w_two_contexts
    c_w_one = sum([x.count for x in w_one])
    c_w_two = sum([x.count for x in w_two])
    #print(c_w_one)
    #print(c_w_two)
    context_ent = [entropy_calc(float(c_w_one),float(c_w_two),
                                float(w_one_contexts[x]),float(w_two_contexts[x])) for x in w_one_contexts]
    #print context_ent
    #print(context_ent)
    context_sum = sum(context_ent)
    #print(context_sum)
    return context_sum


def entropy_calc(cntOne,cntTwo,cntCOne,cntCTwo):
    #print cntOne
    #print cntTwo
    #print cntCOne
    #print cntCTwo
    pCGivenWords = (cntCOne + cntCTwo)/(cntOne + cntTwo)
    Entp = cntCOne / (cntCOne + cntCTwo)
    if Entp == 0.0:
        Entp = 0.0000001
    elif Entp == 1.0:
        Entp = 0.9999999
    HWordsGivenC = - (Entp * math.log(Entp)) - ((1-Entp) * math.log(1-Entp))
    return pCGivenWords * HWordsGivenC

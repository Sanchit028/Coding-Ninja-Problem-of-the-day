# Terms Of AP

from os import *
from sys import *
from collections import *
from math import *

def termsOfAP(x):
    res=[]
    i=0
    while(i<x):
        a=3*(i+1)+2
        if a%4 == 0:
            x=x+1
        else:
            res.append(a)
        i+=1
    return res
    pass

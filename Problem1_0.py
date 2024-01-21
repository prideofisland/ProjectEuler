# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:55:46 2020

@author: pride
"""
#import time
#start=time.time()
def mult_35(limit):
    sum_35=0;
    for i in range(1,limit):
        if i % 3 == 0 or i%5 == 0:
            sum_35+=i;
    return sum_35

print(mult_35(1000))
#end=time.time()
#print(end - start)

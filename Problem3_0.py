# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:00:24 2020

@author: pride
"""
import math 
def prime_factors(num):
    for i in range(2,math.floor(math.sqrt(num))):
        if num % i == 0:
            yield i
            num=num/i
print([i for i in prime_factors(600851475143 )]) #600851475143
all_prime_factors=[i for i in prime_factors(600851475143)]
print(max(all_prime_factors))
    

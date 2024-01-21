# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:58:34 2024

@author: pride
"""

import math

def prime_factors_list(num):
    factors = []
    
    for i in range(2, (int(math.sqrt(num)) + 1)):
        while num % i == 0:
            factors.append(i)
            num //= i

    if num > 1:
        factors.append(num)

    return factors

num = 600851475143
all_prime_factors = prime_factors_list(num)

print(all_prime_factors)
max_prime_factor = max(all_prime_factors)
print(max_prime_factor)

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:00:08 2020

@author: pride
"""


def divisors(num):
    for i in range(2,num+1):
        if num % i == 0:
            yield i;
def small_div(num):
    new_num=num;
    j=2;
    for i in range(2,num+1):
        if new_num % j == 0:
            new_num= new_num/j;
            yield j;
            j=j;
        else:
            j=j+1;

start_num=2;
first_list=[i for i in small_div(start_num)]
for h in range(3,21):
    next_num=[i for i in small_div(h)]
    for k in range(0,(len(next_num))):
        if next_num.count(next_num[k]) > first_list.count(next_num[k]):
            first_list.append(next_num[k])
sum=1;
for g in range(0,len(first_list)):
    sum=sum*first_list[g]
print('result',sum)


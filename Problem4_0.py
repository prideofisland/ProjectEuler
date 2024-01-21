# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:16:56 2020

@author: pride
"""
def check_palindrome(num):
    num=str(num)
    s1=num[0:3]
    s2=num[3:][::-1]
    return s1 == s2

highest_num=0;
min_num=100;
max_num=1000;
for i in range(min_num,max_num):
    for j in range(min_num,max_num):
        num=i*j;
        if check_palindrome(num) and num>highest_num:
            highest_num=num;
print(highest_num)
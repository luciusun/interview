#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


def fibonacci1(n):
    temp = [0, 1]
    if (n < 2):
        return temp[n]
    fibZero = 0
    fibOne = 1
    # fibN = 0
    i = 1
    while (i < n):
        fibN = fibZero + fibOne
        fibOne, fibZero = fibN, fibOne
        i = i + 1
    return fibN



def fibonacci2(n):
    temp = [0, 1]
    if(n>=2):
        for i in range(2, n+1):
            temp[i%2] = temp[0] + temp[1]
        return temp[n%2]

for i in range(10):
    print(fibonacci2(i))




#打印前十项
def fn(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    result = [1, 1]
    while n > 2:
        tmp = result[-1] + result[-2]
        result.append(tmp)
        n -= 1
    return result

print(fn(10))
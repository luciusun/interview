#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note:
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

__author__ = 'slucius'


def reCover(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n>=2):
        return reCover(n-1)+reCover(n-2)


# print(reCover(10))

def reCover1(n):
    temp = [1, 2]
    if(n<=0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n>=3):
        for i in range(3, n+1):
            temp[(i+1)%2] = temp[0] + temp[1]
        return temp[(n+1)%2]

# for i in range(10):
#     print(reCover1(i))


def reCover2(n):
    temp = [0, 1, 2]
    if(n<=0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n>=3):
        for i in range(3, n+1):
            val = temp[i-1] + temp[i-2]
            temp.append(val)
        return temp[-1]


